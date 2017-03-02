# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimulatorTab(object):
    def setupUi(self, SimulatorTab):
        SimulatorTab.setObjectName("SimulatorTab")
        SimulatorTab.resize(1083, 551)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SimulatorTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(SimulatorTab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_3 = QtWidgets.QFrame(self.splitter_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(self.frame_3)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.treeProtocols = GeneratorTreeView(self.frame_3)
        self.treeProtocols.setObjectName("treeProtocols")
        self.verticalLayout_3.addWidget(self.treeProtocols)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.frame_4 = QtWidgets.QFrame(self.splitter_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gvSimulator = SimulatorGraphicsView(self.frame_4)
        self.gvSimulator.setObjectName("gvSimulator")
        self.gridLayout_3.addWidget(self.gvSimulator, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.splitter_2)
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.tblViewFieldValues = QtWidgets.QTableView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblViewFieldValues.sizePolicy().hasHeightForWidth())
        self.tblViewFieldValues.setSizePolicy(sizePolicy)
        self.tblViewFieldValues.setAlternatingRowColors(True)
        self.tblViewFieldValues.setShowGrid(False)
        self.tblViewFieldValues.setObjectName("tblViewFieldValues")
        self.tblViewFieldValues.horizontalHeader().setVisible(True)
        self.tblViewFieldValues.horizontalHeader().setCascadingSectionResizes(False)
        self.tblViewFieldValues.horizontalHeader().setDefaultSectionSize(150)
        self.tblViewFieldValues.horizontalHeader().setStretchLastSection(True)
        self.tblViewFieldValues.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tblViewFieldValues, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(SimulatorTab)
        QtCore.QMetaObject.connectSlotsByName(SimulatorTab)

    def retranslateUi(self, SimulatorTab):
        _translate = QtCore.QCoreApplication.translate
        SimulatorTab.setWindowTitle(_translate("SimulatorTab", "Form"))
        self.label.setText(_translate("SimulatorTab", "Protocols:"))
        self.toolButton.setText(_translate("SimulatorTab", "..."))
        self.pushButton.setText(_translate("SimulatorTab", "Start simulation ..."))
        self.label_8.setText(_translate("SimulatorTab", "<html><head/><body><p><span style=\" font-weight:600;\">Message fields for messsage #</span></p></body></html>"))

from urh.ui.views.GeneratorTreeView import GeneratorTreeView
from urh.ui.views.SimulatorGraphicsView import SimulatorGraphicsView
from . import urh_rc
