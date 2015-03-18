# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:35:56 2013

@author: Steven Wu, Mark Harrison
"""

from PyQt4.QtCore import QPointF
import math

from RbElementCommon import sanitizeName

class BeamlineCommon(object):
    def __init__(self, data = None):
        if data is None:
            self.setName('B')
            self.data = []
        else:
            self.setName(data[0])
            self.data = data[1:]

    def isBeamline(self):
        return True
            
    def getName(self):
        return self._name

    def setName(self, newName):
        self._name = sanitizeName(newName)

    name = property(getName, setName)


    def addElement(self, newElement):
        self.data.append(newElement)
                
    def reverse(self):
        return ReverseBeamline(self)

    def picture(self, scene, beamPosition = QPointF(0,0), angle = 0):
        for element in self.data:
            beamPosition, angle = element.picture(scene, beamPosition, angle) 
        return beamPosition, angle            

    def displayLine(self):
        return 'LINE=(' + ','.join(element.name for element in self.data) + ')'

    def contains(self, searchElement):
        if searchElement is self or searchElement in self.data:
            return True

        return any([element.contains(searchElement) for element in self.data])

    def getLength(self):
        return math.fsum([element.getLength() for element in self.data])

    def getAngle(self):
        return math.fsum([element.getAngle() for element in self.data])

    def getNumberOfElements(self):
        return sum([element.getNumberOfElements() for element in self.data])

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if self.name != other.name:
            return False
        return self.data == other.data

    def __ne__(self, other):
        return not self == other

class ReverseBeamline(object):
    def __init__(self, beamline):
        self.originalBeamline = beamline

    def isBeamline(self):
        return True

    def getName(self):
        return '-' + self.originalBeamline.name

    name = property(getName)

    def reverse(self):
        return self.originalBeamline

    # Recursively reverse contained beamlines for drawing
    def picture(self, scene, beamPosition = QPointF(0,0), angle = 0):
        for element in reversed(self.originalBeamline.data):
            beamPosition, angle = element.reverse().picture(scene, beamPosition, angle)
        return beamPosition, angle

    def contains(self, searchElement):
        return self.originalBeamline.contains(searchElement)

    def getLength(self):
        return self.originalBeamline.getLength()

    def getAngle(self):
        return self.originalBeamline.getAngle()

    def getNumberOfElements(self):
        return self.originalBeamline.getNumberOfElements()

    def __eq__(self, other):
        return self.originalBeamline == other.originalBeamline

    def __ne__(self, other):
        return not self == other