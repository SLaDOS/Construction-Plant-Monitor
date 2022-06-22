# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MonitorWindow(object):
    def setupUi(self, MonitorWindow):
        MonitorWindow.setObjectName("MonitorWindow")
        MonitorWindow.resize(1224, 838)
        self.centralwidget = QtWidgets.QWidget(MonitorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 611, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(610, 0, 611, 521))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.ignoreButton = QtWidgets.QPushButton(self.centralwidget)
        self.ignoreButton.setGeometry(QtCore.QRect(1030, 580, 81, 23))
        self.ignoreButton.setObjectName("ignoreButton")
        self.commitButton = QtWidgets.QPushButton(self.centralwidget)
        self.commitButton.setGeometry(QtCore.QRect(760, 620, 81, 23))
        self.commitButton.setObjectName("commitButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(710, 570, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        MonitorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MonitorWindow)
        self.statusbar.setObjectName("statusbar")
        MonitorWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MonitorWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1224, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MonitorWindow.setMenuBar(self.menuBar)
        self.action1 = QtWidgets.QAction(MonitorWindow)
        self.action1.setObjectName("action1")
        self.menu.addAction(self.action1)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MonitorWindow)
        QtCore.QMetaObject.connectSlotsByName(MonitorWindow)

    def retranslateUi(self, MonitorWindow):
        _translate = QtCore.QCoreApplication.translate
        MonitorWindow.setWindowTitle(_translate("MonitorWindow", "MonitorWindow"))
        self.ignoreButton.setText(_translate("MonitorWindow", "忽略"))
        self.commitButton.setText(_translate("MonitorWindow", "记录"))
        self.menu.setTitle(_translate("MonitorWindow", "测试"))
        self.action1.setText(_translate("MonitorWindow", "导入图片"))

