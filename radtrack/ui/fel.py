# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fel.ui'
#
# Created: Mon May 04 21:19:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1186, 550)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ymin = QtGui.QLineEdit(Form)
        self.ymin.setObjectName(_fromUtf8("ymin"))
        self.gridLayout_2.addWidget(self.ymin, 3, 2, 1, 1)
        self.label_41 = QtGui.QLabel(Form)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_2.addWidget(self.label_41, 3, 0, 1, 1)
        self.label_42 = QtGui.QLabel(Form)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_2.addWidget(self.label_42, 4, 0, 1, 1)
        self.z = QtGui.QComboBox(Form)
        self.z.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.z.setObjectName(_fromUtf8("z"))
        self.gridLayout_2.addWidget(self.z, 4, 1, 1, 1)
        self.ymax = QtGui.QLineEdit(Form)
        self.ymax.setObjectName(_fromUtf8("ymax"))
        self.gridLayout_2.addWidget(self.ymax, 3, 3, 1, 1)
        self.y = QtGui.QComboBox(Form)
        self.y.setObjectName(_fromUtf8("y"))
        self.gridLayout_2.addWidget(self.y, 3, 1, 1, 1)
        self.xmax = QtGui.QLineEdit(Form)
        self.xmax.setObjectName(_fromUtf8("xmax"))
        self.gridLayout_2.addWidget(self.xmax, 1, 3, 1, 1)
        self.label_40 = QtGui.QLabel(Form)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_2.addWidget(self.label_40, 1, 0, 1, 1)
        self.x = QtGui.QComboBox(Form)
        self.x.setObjectName(_fromUtf8("x"))
        self.gridLayout_2.addWidget(self.x, 1, 1, 1, 1)
        self.xmin = QtGui.QLineEdit(Form)
        self.xmin.setObjectName(_fromUtf8("xmin"))
        self.gridLayout_2.addWidget(self.xmin, 1, 2, 1, 1)
        self.label_43 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_2.addWidget(self.label_43, 0, 2, 1, 1)
        self.label_44 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_2.addWidget(self.label_44, 0, 3, 1, 1)
        self.plotButton = QtGui.QPushButton(Form)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.gridLayout_2.addWidget(self.plotButton, 5, 1, 1, 3)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 6, 1, 1)
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 1, 5, 2, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_45 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_4.addWidget(self.label_45, 0, 1, 1, 4)
        self.solverResult = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solverResult.sizePolicy().hasHeightForWidth())
        self.solverResult.setSizePolicy(sizePolicy)
        self.solverResult.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.solverResult.setText(_fromUtf8(""))
        self.solverResult.setReadOnly(True)
        self.solverResult.setObjectName(_fromUtf8("solverResult"))
        self.gridLayout_4.addWidget(self.solverResult, 3, 2, 1, 3)
        self.label_48 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_4.addWidget(self.label_48, 2, 1, 1, 1)
        self.target = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target.sizePolicy().hasHeightForWidth())
        self.target.setSizePolicy(sizePolicy)
        self.target.setObjectName(_fromUtf8("target"))
        self.gridLayout_4.addWidget(self.target, 1, 2, 1, 1)
        self.label_47 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.gridLayout_4.addWidget(self.label_47, 1, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_4.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.solve = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solve.sizePolicy().hasHeightForWidth())
        self.solve.setSizePolicy(sizePolicy)
        self.solve.setObjectName(_fromUtf8("solve"))
        self.gridLayout_4.addWidget(self.solve, 3, 1, 1, 1)
        self.label_46 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_4.addWidget(self.label_46, 1, 1, 1, 1)
        self.vary = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vary.sizePolicy().hasHeightForWidth())
        self.vary.setSizePolicy(sizePolicy)
        self.vary.setObjectName(_fromUtf8("vary"))
        self.gridLayout_4.addWidget(self.vary, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 3)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_27 = QtGui.QLabel(Form)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_27)
        self.raleigh = QtGui.QLineEdit(Form)
        self.raleigh.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.raleigh.setReadOnly(True)
        self.raleigh.setObjectName(_fromUtf8("raleigh"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.raleigh)
        self.label_28 = QtGui.QLabel(Form)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_28)
        self.photonemit = QtGui.QLineEdit(Form)
        self.photonemit.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.photonemit.setReadOnly(True)
        self.photonemit.setObjectName(_fromUtf8("photonemit"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.photonemit)
        self.label_29 = QtGui.QLabel(Form)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_29)
        self.fel_1d = QtGui.QLineEdit(Form)
        self.fel_1d.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.fel_1d.setReadOnly(True)
        self.fel_1d.setObjectName(_fromUtf8("fel_1d"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.fel_1d)
        self.label_30 = QtGui.QLabel(Form)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_30)
        self.gain_1d = QtGui.QLineEdit(Form)
        self.gain_1d.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.gain_1d.setReadOnly(True)
        self.gain_1d.setObjectName(_fromUtf8("gain_1d"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.gain_1d)
        self.label_31 = QtGui.QLabel(Form)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_31)
        self.dfactor = QtGui.QLineEdit(Form)
        self.dfactor.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.dfactor.setReadOnly(True)
        self.dfactor.setObjectName(_fromUtf8("dfactor"))
        self.formLayout_6.setWidget(5, QtGui.QFormLayout.FieldRole, self.dfactor)
        self.label_32 = QtGui.QLabel(Form)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.formLayout_6.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_32)
        self.efactor = QtGui.QLineEdit(Form)
        self.efactor.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.efactor.setReadOnly(True)
        self.efactor.setObjectName(_fromUtf8("efactor"))
        self.formLayout_6.setWidget(6, QtGui.QFormLayout.FieldRole, self.efactor)
        self.label_33 = QtGui.QLabel(Form)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.formLayout_6.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_33)
        self.espreadfactor = QtGui.QLineEdit(Form)
        self.espreadfactor.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.espreadfactor.setReadOnly(True)
        self.espreadfactor.setObjectName(_fromUtf8("espreadfactor"))
        self.formLayout_6.setWidget(7, QtGui.QFormLayout.FieldRole, self.espreadfactor)
        self.label_37 = QtGui.QLabel(Form)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.formLayout_6.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_37)
        self.sasepower = QtGui.QLineEdit(Form)
        self.sasepower.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.sasepower.setReadOnly(True)
        self.sasepower.setObjectName(_fromUtf8("sasepower"))
        self.formLayout_6.setWidget(8, QtGui.QFormLayout.FieldRole, self.sasepower)
        self.label_38 = QtGui.QLabel(Form)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.formLayout_6.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_38)
        self.saseenergy = QtGui.QLineEdit(Form)
        self.saseenergy.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.saseenergy.setReadOnly(True)
        self.saseenergy.setObjectName(_fromUtf8("saseenergy"))
        self.formLayout_6.setWidget(9, QtGui.QFormLayout.FieldRole, self.saseenergy)
        self.label_34 = QtGui.QLabel(Form)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.formLayout_6.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_34)
        self.threedfel = QtGui.QLineEdit(Form)
        self.threedfel.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.threedfel.setReadOnly(True)
        self.threedfel.setObjectName(_fromUtf8("threedfel"))
        self.formLayout_6.setWidget(10, QtGui.QFormLayout.FieldRole, self.threedfel)
        self.label_35 = QtGui.QLabel(Form)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.formLayout_6.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_35)
        self.gain_3d = QtGui.QLineEdit(Form)
        self.gain_3d.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.gain_3d.setReadOnly(True)
        self.gain_3d.setObjectName(_fromUtf8("gain_3d"))
        self.formLayout_6.setWidget(11, QtGui.QFormLayout.FieldRole, self.gain_3d)
        self.label_36 = QtGui.QLabel(Form)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.formLayout_6.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_36)
        self.total = QtGui.QLineEdit(Form)
        self.total.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.total.setReadOnly(True)
        self.total.setObjectName(_fromUtf8("total"))
        self.formLayout_6.setWidget(12, QtGui.QFormLayout.FieldRole, self.total)
        self.label_26 = QtGui.QLabel(Form)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_26)
        self.label_22 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout_6.setWidget(13, QtGui.QFormLayout.SpanningRole, self.label_22)
        self.label_23 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_6.setWidget(14, QtGui.QFormLayout.LabelRole, self.label_23)
        self.averagepower = QtGui.QLineEdit(Form)
        self.averagepower.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.averagepower.setReadOnly(True)
        self.averagepower.setObjectName(_fromUtf8("averagepower"))
        self.formLayout_6.setWidget(14, QtGui.QFormLayout.FieldRole, self.averagepower)
        self.label_25 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_6.setWidget(15, QtGui.QFormLayout.LabelRole, self.label_25)
        self.saturation = QtGui.QLineEdit(Form)
        self.saturation.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.saturation.setReadOnly(True)
        self.saturation.setObjectName(_fromUtf8("saturation"))
        self.formLayout_6.setWidget(15, QtGui.QFormLayout.FieldRole, self.saturation)
        self.gridLayout.addLayout(self.formLayout_6, 1, 4, 2, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.charge = QtGui.QLineEdit(Form)
        self.charge.setObjectName(_fromUtf8("charge"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.charge)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.slicemit = QtGui.QLineEdit(Form)
        self.slicemit.setObjectName(_fromUtf8("slicemit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.slicemit)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.ebeamenergy = QtGui.QLineEdit(Form)
        self.ebeamenergy.setObjectName(_fromUtf8("ebeamenergy"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.ebeamenergy)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.energyspread = QtGui.QLineEdit(Form)
        self.energyspread.setObjectName(_fromUtf8("energyspread"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.energyspread)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.reprate = QtGui.QLineEdit(Form)
        self.reprate.setObjectName(_fromUtf8("reprate"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.reprate)
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_17)
        self.peakamp = QtGui.QLineEdit(Form)
        self.peakamp.setStyleSheet(_fromUtf8(""))
        self.peakamp.setReadOnly(False)
        self.peakamp.setObjectName(_fromUtf8("peakamp"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.peakamp)
        self.label_8 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.label_8)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_10)
        self.ufield = QtGui.QLineEdit(Form)
        self.ufield.setObjectName(_fromUtf8("ufield"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.ufield)
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_11)
        self.beta = QtGui.QLineEdit(Form)
        self.beta.setObjectName(_fromUtf8("beta"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.beta)
        self.label_24 = QtGui.QLabel(Form)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_24)
        self.radiatedwavelength = QtGui.QLineEdit(Form)
        self.radiatedwavelength.setStyleSheet(_fromUtf8(""))
        self.radiatedwavelength.setReadOnly(False)
        self.radiatedwavelength.setObjectName(_fromUtf8("radiatedwavelength"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.radiatedwavelength)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_13)
        self.bunlen = QtGui.QLineEdit(Form)
        self.bunlen.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.bunlen.setReadOnly(True)
        self.bunlen.setObjectName(_fromUtf8("bunlen"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.bunlen)
        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.gamma = QtGui.QLineEdit(Form)
        self.gamma.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.gamma.setReadOnly(True)
        self.gamma.setObjectName(_fromUtf8("gamma"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.gamma)
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self.edensity = QtGui.QLineEdit(Form)
        self.edensity.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.edensity.setReadOnly(True)
        self.edensity.setObjectName(_fromUtf8("edensity"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.edensity)
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_16)
        self.geoemit = QtGui.QLineEdit(Form)
        self.geoemit.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.geoemit.setReadOnly(True)
        self.geoemit.setObjectName(_fromUtf8("geoemit"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.geoemit)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.bunchlen = QtGui.QLineEdit(Form)
        self.bunchlen.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.bunchlen.setReadOnly(True)
        self.bunchlen.setObjectName(_fromUtf8("bunchlen"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.bunchlen)
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.SpanningRole, self.label_18)
        self.label_19 = QtGui.QLabel(Form)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_19)
        self.rmssize = QtGui.QLineEdit(Form)
        self.rmssize.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.rmssize.setReadOnly(True)
        self.rmssize.setObjectName(_fromUtf8("rmssize"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.rmssize)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.uperiod = QtGui.QLineEdit(Form)
        self.uperiod.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.uperiod.setReadOnly(True)
        self.uperiod.setObjectName(_fromUtf8("uperiod"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.uperiod)
        self.label_20 = QtGui.QLabel(Form)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_20)
        self.uparam = QtGui.QLineEdit(Form)
        self.uparam.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.uparam.setReadOnly(True)
        self.uparam.setObjectName(_fromUtf8("uparam"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.FieldRole, self.uparam)
        self.label_21 = QtGui.QLabel(Form)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_21)
        self.uwave = QtGui.QLineEdit(Form)
        self.uwave.setStyleSheet(_fromUtf8("background-color: rgb(225, 225, 225);"))
        self.uwave.setReadOnly(True)
        self.uwave.setObjectName(_fromUtf8("uwave"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.FieldRole, self.uwave)
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_12)
        self.gridLayout.addLayout(self.formLayout_3, 1, 2, 1, 1)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 3, 2, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 5)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.plotWidget = matplotlibWidget(Form)
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.gridLayout_3.addWidget(self.plotWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 6, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_41.setText(_translate("Form", "y:", None))
        self.label_42.setText(_translate("Form", "z:", None))
        self.label_40.setText(_translate("Form", "x:", None))
        self.label_43.setText(_translate("Form", "min", None))
        self.label_44.setText(_translate("Form", "max", None))
        self.plotButton.setText(_translate("Form", "Plot", None))
        self.label_45.setText(_translate("Form", "FEL Solver", None))
        self.label_48.setText(_translate("Form", "Variable:", None))
        self.label_47.setText(_translate("Form", "Goal:", None))
        self.solve.setText(_translate("Form", "Solve", None))
        self.label_46.setText(_translate("Form", "Value:", None))
        self.label_27.setText(_translate("Form", "Rayleigh range:", None))
        self.raleigh.setToolTip(_translate("Form", "cm", None))
        self.label_28.setText(_translate("Form", "Photon emittance:", None))
        self.photonemit.setToolTip(_translate("Form", "nm", None))
        self.label_29.setText(_translate("Form", "1D FEL parameter:", None))
        self.label_30.setText(_translate("Form", "1D gain length:", None))
        self.gain_1d.setToolTip(_translate("Form", "cm", None))
        self.label_31.setText(_translate("Form", "Diffraction factor:", None))
        self.label_32.setText(_translate("Form", "Emittance factor:", None))
        self.label_33.setText(_translate("Form", "Energy spread factor:", None))
        self.label_37.setText(_translate("Form", "SASE power at saturation:", None))
        self.sasepower.setToolTip(_translate("Form", "GW", None))
        self.label_38.setText(_translate("Form", "SASE pulsed energy:", None))
        self.saseenergy.setToolTip(_translate("Form", "mJ", None))
        self.label_34.setText(_translate("Form", "3D FEL parameter:", None))
        self.label_35.setText(_translate("Form", "3D gain length:", None))
        self.gain_3d.setToolTip(_translate("Form", "cm", None))
        self.label_36.setText(_translate("Form", "3D effect total:", None))
        self.label_26.setText(_translate("Form", "FEL Performance", None))
        self.label_22.setText(_translate("Form", "FEL Output", None))
        self.label_23.setText(_translate("Form", "Average power:", None))
        self.averagepower.setToolTip(_translate("Form", "W", None))
        self.label_25.setText(_translate("Form", "Saturation length:", None))
        self.saturation.setToolTip(_translate("Form", "m", None))
        self.label.setText(_translate("Form", "E-Beam Inputs", None))
        self.label_2.setText(_translate("Form", "Charge:", None))
        self.charge.setToolTip(_translate("Form", "pC", None))
        self.label_3.setText(_translate("Form", "Normalized sliced emittance: ", None))
        self.slicemit.setToolTip(_translate("Form", "mm-mrad", None))
        self.label_4.setText(_translate("Form", "E-beam energy:", None))
        self.ebeamenergy.setToolTip(_translate("Form", "MeV", None))
        self.label_5.setText(_translate("Form", "Sliced energy spread:", None))
        self.energyspread.setToolTip(_translate("Form", "%", None))
        self.label_7.setText(_translate("Form", "Repetition rate:", None))
        self.label_17.setText(_translate("Form", "Peak current:", None))
        self.peakamp.setToolTip(_translate("Form", "A", None))
        self.label_8.setText(_translate("Form", "Undulator and Focusing Inputs", None))
        self.label_10.setText(_translate("Form", "Undulator field:", None))
        self.ufield.setToolTip(_translate("Form", "T", None))
        self.label_11.setText(_translate("Form", "Average beta function:", None))
        self.beta.setToolTip(_translate("Form", "m", None))
        self.label_24.setText(_translate("Form", "Radiated wavelength:", None))
        self.radiatedwavelength.setToolTip(_translate("Form", "nm", None))
        self.label_13.setText(_translate("Form", "Bunch length(distance):", None))
        self.bunlen.setToolTip(_translate("Form", "FWHM", None))
        self.label_14.setText(_translate("Form", "Gamma:", None))
        self.label_15.setText(_translate("Form", "Peak electron density:", None))
        self.edensity.setToolTip(_translate("Form", "1/m^3", None))
        self.label_16.setText(_translate("Form", "Geometric emittance:", None))
        self.geoemit.setToolTip(_translate("Form", "nm", None))
        self.label_6.setText(_translate("Form", "Bunch length(time):", None))
        self.bunchlen.setToolTip(_translate("Form", "FWHM", None))
        self.label_18.setText(_translate("Form", "Undulator and Focusing Parameters", None))
        self.label_19.setText(_translate("Form", "RMS beam size(average):", None))
        self.rmssize.setToolTip(_translate("Form", "um", None))
        self.label_9.setText(_translate("Form", "Undulator period:", None))
        self.uperiod.setToolTip(_translate("Form", "mm", None))
        self.label_20.setText(_translate("Form", "Undulator parameter:", None))
        self.label_21.setText(_translate("Form", "Undulator wavenumber:", None))
        self.uwave.setToolTip(_translate("Form", "1/m", None))
        self.label_12.setText(_translate("Form", "E-Beam Parameters", None))

from radtrack.gui.matplotlibwidget import matplotlibWidget
