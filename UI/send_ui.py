# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_ui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SendDialog(object):
    def setupUi(self, SendDialog):
        SendDialog.setObjectName("SendDialog")
        SendDialog.resize(329, 96)
        self.ProgBar = QtWidgets.QProgressBar(SendDialog)
        self.ProgBar.setGeometry(QtCore.QRect(16, 32, 297, 25))
        self.ProgBar.setProperty("value", 24)
        self.ProgBar.setObjectName("ProgBar")
        self.SelectBtn = QtWidgets.QToolButton(SendDialog)
        self.SelectBtn.setGeometry(QtCore.QRect(16, 8, 65, 22))
        self.SelectBtn.setObjectName("SelectBtn")
        self.SendBtn = QtWidgets.QPushButton(SendDialog)
        self.SendBtn.setGeometry(QtCore.QRect(232, 56, 81, 32))
        self.SendBtn.setObjectName("SendBtn")
        self.SendLog = QtWidgets.QLabel(SendDialog)
        self.SendLog.setGeometry(QtCore.QRect(16, 56, 209, 16))
        self.SendLog.setText("")
        self.SendLog.setObjectName("SendLog")

        self.retranslateUi(SendDialog)
        QtCore.QMetaObject.connectSlotsByName(SendDialog)

    def retranslateUi(self, SendDialog):
        _translate = QtCore.QCoreApplication.translate
        SendDialog.setWindowTitle(_translate("SendDialog", "Dialog"))
        self.SelectBtn.setText(_translate("SendDialog", "Select File"))
        self.SendBtn.setText(_translate("SendDialog", "Send"))

