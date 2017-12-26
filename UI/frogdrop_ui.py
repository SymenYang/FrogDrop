# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frogdrop_ui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrogDrop(object):
    def setupUi(self, FrogDrop):
        FrogDrop.setObjectName("FrogDrop")
        FrogDrop.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(FrogDrop)
        self.centralwidget.setObjectName("centralwidget")
        self.RecList = QtWidgets.QGroupBox(self.centralwidget)
        self.RecList.setGeometry(QtCore.QRect(16, 120, 265, 249))
        self.RecList.setTitle("")
        self.RecList.setObjectName("RecList")
        self.ChooseBtn = QtWidgets.QPushButton(self.RecList)
        self.ChooseBtn.setGeometry(QtCore.QRect(140, 216, 71, 32))
        self.ChooseBtn.setObjectName("ChooseBtn")
        self.RefreshBtn = QtWidgets.QPushButton(self.RecList)
        self.RefreshBtn.setGeometry(QtCore.QRect(50, 216, 71, 32))
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.RecHeadline = QtWidgets.QLabel(self.RecList)
        self.RecHeadline.setGeometry(QtCore.QRect(40, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.RecHeadline.setFont(font)
        self.RecHeadline.setObjectName("RecHeadline")
        self.RecTable = QtWidgets.QTableWidget(self.RecList)
        self.RecTable.setGeometry(QtCore.QRect(8, 32, 249, 185))
        self.RecTable.setObjectName("RecTable")
        self.RecTable.setColumnCount(0)
        self.RecTable.setRowCount(0)
        self.LocalHost = QtWidgets.QGroupBox(self.centralwidget)
        self.LocalHost.setGeometry(QtCore.QRect(20, 60, 225, 51))
        self.LocalHost.setTitle("")
        self.LocalHost.setObjectName("LocalHost")
        self.NameLabel = QtWidgets.QLabel(self.LocalHost)
        self.NameLabel.setGeometry(QtCore.QRect(60, 0, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.HostIP = QtWidgets.QLabel(self.LocalHost)
        self.HostIP.setGeometry(QtCore.QRect(60, 24, 161, 20))
        self.HostIP.setObjectName("HostIP")
        self.HeadPic = QtWidgets.QLabel(self.LocalHost)
        self.HeadPic.setGeometry(QtCore.QRect(0, 0, 49, 49))
        self.HeadPic.setObjectName("HeadPic")
        self.EditBtn = QtWidgets.QToolButton(self.centralwidget)
        self.EditBtn.setGeometry(QtCore.QRect(256, 64, 26, 22))
        self.EditBtn.setObjectName("EditBtn")
        self.LogoPic = QtWidgets.QLabel(self.centralwidget)
        self.LogoPic.setGeometry(QtCore.QRect(83, 7, 133, 43))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.LogoPic.setFont(font)
        self.LogoPic.setObjectName("LogoPic")
        FrogDrop.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FrogDrop)
        self.statusbar.setObjectName("statusbar")
        FrogDrop.setStatusBar(self.statusbar)

        self.retranslateUi(FrogDrop)
        QtCore.QMetaObject.connectSlotsByName(FrogDrop)

    def retranslateUi(self, FrogDrop):
        _translate = QtCore.QCoreApplication.translate
        FrogDrop.setWindowTitle(_translate("FrogDrop", "MainWindow"))
        self.ChooseBtn.setText(_translate("FrogDrop", "Choose"))
        self.RefreshBtn.setText(_translate("FrogDrop", "Refresh"))
        self.RecHeadline.setText(_translate("FrogDrop", "Choose your receiver:)"))
        self.NameLabel.setText(_translate("FrogDrop", "Your name"))
        self.HostIP.setText(_translate("FrogDrop", "local host"))
        self.HeadPic.setText(_translate("FrogDrop", "Pic"))
        self.EditBtn.setText(_translate("FrogDrop", "edit"))
        self.LogoPic.setText(_translate("FrogDrop", "Frog Drop"))

