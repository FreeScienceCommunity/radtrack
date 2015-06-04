# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsrw.ui'
#
# Created: Fri May  8 14:02:42 2015
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
    def setupUi(self, Form, is_multi_particle=False):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1060, 602)
        self.is_multi_particle = is_multi_particle
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 171, 561))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.precision = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.precision.sizePolicy().hasHeightForWidth())
        self.precision.setSizePolicy(sizePolicy)
        self.precision.setObjectName(_fromUtf8("precision"))
        self.verticalLayout.addWidget(self.precision)
        self.undulator = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undulator.sizePolicy().hasHeightForWidth())
        self.undulator.setSizePolicy(sizePolicy)
        self.undulator.setObjectName(_fromUtf8("undulator"))
        self.verticalLayout.addWidget(self.undulator)
        self.beam = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beam.sizePolicy().hasHeightForWidth())
        self.beam.setSizePolicy(sizePolicy)
        self.beam.setObjectName(_fromUtf8("beam"))
        self.verticalLayout.addWidget(self.beam)
        self.analyze = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyze.sizePolicy().hasHeightForWidth())
        self.analyze.setSizePolicy(sizePolicy)
        self.analyze.setObjectName(_fromUtf8("analyze"))
        self.verticalLayout.addWidget(self.analyze)
        self.sim = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sim.sizePolicy().hasHeightForWidth())
        self.sim.setSizePolicy(sizePolicy)
        self.sim.setObjectName(_fromUtf8("sim"))
        self.verticalLayout.addWidget(self.sim)
        self.formLayoutWidget_4 = QtGui.QWidget(Form)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(200, 40, 291, 82))
        self.formLayoutWidget_4.setObjectName(_fromUtf8("formLayoutWidget_4"))
        self.formLayout_4 = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setMargin(0)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        if not self.is_multi_particle:
            self.label_31 = QtGui.QLabel(self.formLayoutWidget_4)
            self.label_31.setObjectName(_fromUtf8("label_31"))
            self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_31)
            self.label_32 = QtGui.QLabel(self.formLayoutWidget_4)
            self.label_32.setObjectName(_fromUtf8("label_32"))
            self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_32)
            self.intensity = QtGui.QComboBox(self.formLayoutWidget_4)
            self.intensity.setObjectName(_fromUtf8("intensity"))
            self.intensity.addItem(_fromUtf8(""))
            self.intensity.addItem(_fromUtf8(""))
            self.intensity.addItem(_fromUtf8(""))
            self.intensity.addItem(_fromUtf8(""))
            self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.intensity)
        self.label_33 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_33)
        self.deparg = QtGui.QComboBox(self.formLayoutWidget_4)
        self.deparg.setObjectName(_fromUtf8("deparg"))
        for f in range(4 if is_multi_particle else 7):
            self.deparg.addItem(_fromUtf8(""))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.deparg)
        if not self.is_multi_particle:
            self.polar = QtGui.QComboBox(self.formLayoutWidget_4)
            self.polar.setObjectName(_fromUtf8("polar"))
            self.polar.addItem(_fromUtf8(""))
            self.polar.addItem(_fromUtf8(""))
            self.polar.addItem(_fromUtf8(""))
            self.polar.addItem(_fromUtf8(""))
            self.polar.addItem(_fromUtf8(""))
            self.polar.addItem(_fromUtf8(""))
            self.polar.addItem(_fromUtf8(""))
            self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.polar)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(210, 130, 271, 321))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.status = QtGui.QTextEdit(Form)
        self.status.setGeometry(QtCore.QRect(500, 40, 251, 411))
        self.status.setObjectName(_fromUtf8("status"))
        self.analytic = QtGui.QTextEdit(Form)
        self.analytic.setGeometry(QtCore.QRect(780, 40, 251, 411))
        self.analytic.setObjectName(_fromUtf8("analytic"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(850, 20, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.precision.setText(_translate("Form", "Precision", None))
        self.undulator.setText(_translate("Form", "Undulator", None))
        self.beam.setText(_translate("Form", "Beam", None))
        self.analyze.setText(_translate("Form", "Analyze", None))
        self.sim.setText(_translate("Form", "Simulate", None))
        if not self.is_multi_particle:
            self.label_31.setText(_translate("Form", "Polarization", None))
            self.label_32.setText(_translate("Form", "Intensity", None))
            self.intensity.setItemText(0, _translate("Form", "Single Electron Intensity", None))
            self.intensity.setItemText(1, _translate("Form", "Single Electron Flux", None))
            self.intensity.setItemText(2, _translate("Form", "Real Part of Electron E-Field", None))
            self.intensity.setItemText(3, _translate("Form", "Imaginary Part of Electron E-Field", None))
        self.label_33.setText(_translate("Form", "Dependent Argument", None))
        self.deparg.setItemText(0, _translate("Form", "e (energy)", None))
        self.deparg.setItemText(1, _translate("Form", "x (horizontal)", None))
        self.deparg.setItemText(2, _translate("Form", "y (vertical)", None))
        self.deparg.setItemText(3, _translate("Form", "x & y", None))
        if not self.is_multi_particle:
            self.deparg.setItemText(4, _translate("Form", "e & x", None))
            self.deparg.setItemText(5, _translate("Form", "e & y", None))
            self.deparg.setItemText(6, _translate("Form", "e & x & y", None))
            self.polar.setItemText(0, _translate("Form", "Linear Horizontal", None))
            self.polar.setItemText(1, _translate("Form", "Linear Vertical", None))
            self.polar.setItemText(2, _translate("Form", "Linear 45 Degrees", None))
            self.polar.setItemText(3, _translate("Form", "Linear 135 Degrees", None))
            self.polar.setItemText(4, _translate("Form", "Circular Right", None))
            self.polar.setItemText(5, _translate("Form", "Circular Left", None))
            self.polar.setItemText(6, _translate("Form", "Total", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Number of points along Energy", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Number of points along X", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Number of points along Y", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "Distance to Window", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Inital Photon Energy", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "Final Photon Energy", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "Window Left Edge", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "Window Top Edge", None))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "Window Right Edge", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "WIndow Bottom Edge", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "sampling", None))
        self.label.setText(_translate("Form", "Status", None))
        self.label_2.setText(_translate("Form", "Analytic Calculations", None))
