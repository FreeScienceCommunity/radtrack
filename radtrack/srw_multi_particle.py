# -*- coding: utf-8 -*-
u"""Multiparticle SRW Pane

:copyright: Copyright (c) 2013-2015 RadiaBeam Technologies LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from io import open

import array
import copy
import math
import os
import re
import sys

from pykern import pkarray
from pykern import pkcompat
from pykern.pkdebug import pkdc, pkdi, pkdp
import xlrd

from radtrack import RbUtility
from radtrack import rt_controller
from radtrack import rt_jinja
from radtrack import rt_params
from radtrack import rt_popup
from radtrack import srw_enums
from radtrack import srw_pane
from radtrack import srw_params
from radtrack.rt_srwlib import srwlib, uti_plot
from radtrack.srw import AnalyticCalc
from radtrack.util import resource

FILE_PREFIX = 'srw'

class Controller(rt_controller.Controller):
    """Implements contol flow for SRW multiparticle tab"""

    ACTION_NAMES = ('Precision', 'Undulator', 'Beam', 'Analyze', 'Simulate')

    def init(self, parent_widget=None):
        # TODO(robnagler) necessary?
        self.declarations = rt_params.declarations(FILE_PREFIX)
        defaults = rt_params.defaults(FILE_PREFIX)
        self.params = rt_params.init_params(
            defaults['Simulation Complexity']['MULTI_PARTICLE'],
            self.declarations,
        )
        self._view = srw_pane.View(self, parent_widget, is_multi_particle=True)
        return self._view

    def action_analyze(self):
        args = copy.deepcopy(self.params['Undulator'])
        if args['Undulator Orientation'].has_name('VERTICAL'):
            args['Horizontal Magnetic Field'] = 0
            args['Vertical Magnetic Field'] = args['Magnetic Field']
        else:
            args['Horizontal Magnetic Field'] = args['Magnetic Field']
            args['Vertical Magnetic Field'] = 0
        args.update(self.params['Beam'])
        values = AnalyticCalc.multi_particle(args)
        res = rt_jinja.render(
            '''
            Kx: $Kx
            Ky: $Ky
            Wavelength (m)      Phot. energy (eV)
            1st harmonic: $lam_rn   $e_phn
            3rd harmonic: $lam_rn_3   $e_phn_3
            5th harmonic: $lam_rn_5  $e_phn_5
            Critical energy: $E_c eV
            -----------------------------------
            Rad spot size: $RadSpotSize m
            Rad divergence: $RadSpotDivergence rad
            -----------------------------------
            Length of ID: $L_id m
            Radiated power: $P_W W
            Central Power Density:
            $P_Wdc W/mrad2
            Spectral flux:
            $SpectralFluxValue phot/(sec mrad 0.1% BW)
            Spectral Central Brightness:
            $RadBrightness phot/(sec mrad2 0.1% BW)
            -----------------------------------
            ''',
            values,
        )
        self._view.set_result_text('analysis', res)

    def action_beam(self):
        self._pop_up('Beam')

    def action_precision(self):
        self._pop_up('Precision')

    def action_simulate(self):
        msg_list = []
        def msg(m):
            msg_list.append(m + '... \n \n')
            self._view.set_result_text('simulation', ''.join(msg_list))

        (und, magFldCnt) = srw_params.to_undulator(self.params['Undulator'])
        beam = srw_params.to_beam(self.params['Beam'])
        simulation_kind = self._view.current_simulation_kind()
        wp = self.params['Simulation Kind'][simulation_kind.name]['Wavefront']
        stkF = srw_params.to_wavefront(wp)
        stkP = srw_params.to_wavefront(wp)
        pkdc('simulation_kind={}', simulation_kind)
        ar_prec_f = srw_params.to_flux_precision(self.params['Precision'])
        ar_prec_p = srw_params.to_power_precision(self.params['Precision'])

        #for trajectory calculations:

        #Need to reflect in the GUI:
        arPrecPar = [1] #General Precision parameters for Trajectory calculation:
        #[0]: integration method No:
        #1- fourth-order Runge-Kutta (precision is driven by number of points)
        #2- fifth-order Runge-Kutta
        #[1],[2],[3],[4],[5]: absolute precision values for X[m],X'[rad],Y[m],Y'[rad],Z[m] (yet to be tested!!) - to be taken into account only for R-K fifth order or higher
        #[6]: tolerance (default = 1) for R-K fifth order or higher
        #[7]: max. number of auto-steps for R-K fifth order or higher (default = 5000)
        fieldInterpMeth = 4 #Magnetic Field Interpolation Method, to be entered into 3D field structures below (to be used e.g. for trajectory calculation):
        #1- bi-linear (3D), 2- bi-quadratic (3D), 3- bi-cubic (3D), 4- 1D cubic spline (longitudinal) + 2D bi-cubic

        msg('Performing trajectory calculation')
        (Xtrajectory, Ytrajectory, ctMesh) = self._trajectory(
            und,
            magFldCnt,
            arPrecPar,
            fieldInterpMeth,
            beam,
        )
        f = open('Trajectory.txt', 'w')
        f.write(pkcompat.locale_str(Xtrajectory))
        f.write(pkcompat.locale_str(Ytrajectory))
        f.write(pkcompat.locale_str(ctMesh))
#        f.write([str(ctMesh[1]),str(ctMesh[1])])
#        print "%s %s %s " %(str(partTraj.arX),str(partTraj.arY),str(ctMesh))
        f.close()
        msg('Plotting the results')
        msg('NOTE: Close all graph windows to proceed')
        uti_plot.uti_plot_show()

        if simulation_kind.has_name('E'):
            msg('Performing Electric Field (spectrum vs photon energy) calculation')
            pkdc('ar_prec_f={}', ar_prec_f)
            srwlib.srwl.CalcStokesUR(stkF, beam, und, ar_prec_f)
            msg('Extracting Intensity from calculated Electric Field')
            msg('Plotting the results')
            uti_plot.uti_plot1d(
                stkF.arS,
                [stkF.mesh.eStart, stkF.mesh.eFin, stkF.mesh.ne],
                [
                    'Photon Energy [eV]',
                    'Flux [ph/s/.1%bw]',
                    'Flux through Finite Aperture',
                ],
            )
        elif simulation_kind.has_name('X'):
            msg('Performing Power Density calculation (from field) vs x-coordinate calculation')
            pkdc('simulation_kind={}', simulation_kind)
            pkdc('stkP={}', stkP)
            pkdc('beam={}', beam)
            pkdc('und={}', und)
            srwlib.srwl.CalcPowDenSR(stkP, beam, 0, magFldCnt, ar_prec_p)
            msg('Extracting Intensity from calculated Electric Field')
            msg('Plotting the results')
            plotMeshX = [1000*stkP.mesh.xStart, 1000*stkP.mesh.xFin, stkP.mesh.nx]
            powDenVsX = pkarray.new_float([0]*stkP.mesh.nx)
            for i in range(stkP.mesh.nx):
                powDenVsX[i] = stkP.arS[stkP.mesh.nx*int(stkP.mesh.ny*0.5) + i]
            pkdc('plotMeshX={}', plotMeshX)
            uti_plot.uti_plot1d(
                powDenVsX,
                plotMeshX,
                [
                    'Horizontal Position [mm]',
                    'Power Density [W/mm^2]',
                    'Power Density\n(horizontal cut at y = 0)',
                ],
            )
        elif simulation_kind.has_name('Y'):
            msg('Performing Power Density calculation (from field) vs x-coordinate calculation')
            pkdc('simulation_kind={}', simulation_kind)
            pkdc('stkP={}', stkP)
            pkdc('beam={}', beam)
            pkdc('und={}', und)
            srwlib.srwl.CalcPowDenSR(stkP, beam, 0, magFldCnt, ar_prec_p)
            msg('Extracting Intensity from calculated Electric Field')
            msg('Plotting the results')
            plotMeshY = [1000*stkP.mesh.yStart, 1000*stkP.mesh.yFin, stkP.mesh.ny]
            powDenVsY = pkarray.new_float([0]*stkP.mesh.ny)
            for i in range(stkP.mesh.ny):
                powDenVsY[i] = stkP.arS[stkP.mesh.ny*int(stkP.mesh.nx*0.5) + i]
            uti_plot.uti_plot1d(
                powDenVsY,
                plotMeshY,
                [
                    'Vertical Position [mm]',
                    'Power Density [W/mm^2]',
                    'Power Density\n(vertical cut at x = 0)',
                ],
            )
        elif simulation_kind.has_name('X_AND_Y'):
            msg('Performing Electric Field (intensity vs x- and y-coordinate) calculation')
            srwlib.srwl.CalcPowDenSR(stkP, beam, 0, magFldCnt, ar_prec_p)
            msg('Extracting Intensity from calculated Electric Field')
            msg('Plotting the results')
            plotMeshX = [1000*stkP.mesh.xStart, 1000*stkP.mesh.xFin, stkP.mesh.nx]
            plotMeshY = [1000*stkP.mesh.yStart, 1000*stkP.mesh.yFin, stkP.mesh.ny]
            uti_plot.uti_plot2d(
                stkP.arS,
                plotMeshX,
                plotMeshY,
                [
                    'Horizontal Position [mm]',
                    'Vertical Position [mm]',
                    'Power Density',
                ],
            )
        else:
            raise AssertionError('{}: invalid simulation_kind'.format(simulation_kind))
        uti_plot.uti_plot_show()

    def action_undulator(self):
        self._pop_up('Undulator')

    def name_to_action(self, name):
        """Returns button action"""
        return getattr(self, 'action_' + name.lower())

    def _pop_up(self, which):
        pu = rt_popup.Window(
            self.declarations[which],
            self.params[which],
            file_prefix=FILE_PREFIX,
            parent=self._view,
        )
        if pu.exec_():
            self.params[which] = pu.get_params()

    def _trajectory(self,und,magFldCnt,arPrecPar,fieldInterpMeth,beam):
        # Done specifying undulator mag field
        # Initial coordinates of particle trajectory through the ID
        part = srwlib.SRWLParticle()
        part.x = beam.partStatMom1.x
        part.y = beam.partStatMom1.y
        part.xp = beam.partStatMom1.xp
        part.yp = beam.partStatMom1.yp
        part.gamma = 3/0.51099890221e-03 #Relative Energy self.beam.partStatMom1.gamma #
        part.relE0 = 1
        part.nq = -1
        zcID=0

        # number of trajectory points along longitudinal axis
        npTraj = 10001

        #Definitions and allocation for the Trajectory waveform
        part.z = zcID #- 0.5*magFldCnt.MagFld[0].rz
        partTraj = srwlib.SRWLPrtTrj()
        partTraj.partInitCond = part
        partTraj.allocate(npTraj, True)
        partTraj.ctStart = 0
        partTraj.ctEnd = und.nPer*und.per #magFldCnt.MagFld[0].rz
        partTraj = srwlib.srwl.CalcPartTraj(partTraj, magFldCnt, arPrecPar)

        ctMesh = [partTraj.ctStart, partTraj.ctEnd, partTraj.np]
        for i in range(partTraj.np):
            partTraj.arX[i] *= 1000
            partTraj.arY[i] *= 1000
        uti_plot.uti_plot1d(partTraj.arX, ctMesh, ['ct [m]', 'Horizontal Position [mm]'])
        uti_plot.uti_plot1d(partTraj.arY, ctMesh, ['ct [m]', 'Vertical Position [mm]'])
        return (partTraj.arX,partTraj.arY,ctMesh)


Controller.run_if_main()