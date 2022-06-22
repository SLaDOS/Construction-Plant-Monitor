# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_to_monitor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_to_monitor.setObjectName("btn_to_monitor")
        self.verticalLayout.addWidget(self.btn_to_monitor)
        self.btn_to_boss = QtWidgets.QPushButton(self.centralwidget)
        self.btn_to_boss.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_to_boss.setObjectName("btn_to_boss")
        self.verticalLayout.addWidget(self.btn_to_boss)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_to_monitor.setText(_translate("MainWindow", "我是监管者"))
        self.btn_to_boss.setText(_translate("MainWindow", "我是项目负责人"))

