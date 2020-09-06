# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QUI-Lektion3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.inputMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.inputMessage.setGeometry(QtCore.QRect(10, 290, 181, 32))
        self.inputMessage.setObjectName("inputMessage")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 290, 71, 34))
        self.pushButton.setObjectName("pushButton")
        self.inputUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUsername.setGeometry(QtCore.QRect(10, 50, 113, 32))
        self.inputUsername.setObjectName("inputUsername")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 50, 113, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.inputUsername.setText(_translate("MainWindow", "username"))
        self.lineEdit_3.setText(_translate("MainWindow", "password"))
        self.label.setText(_translate("MainWindow", "Messenger"))
