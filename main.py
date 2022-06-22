import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QDesktopWidget, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView

import decision
import img_analysis
import params
import subthread
from gui import ui_main, ui_monitor, ui_boss

img_dir = ""


def select_ui(ui):
    converser.ui = ui


def open_monitor():
    """打开工地管理员面板"""
    ui1 = ui_monitor.Ui_MonitorWindow()
    ui1.setupUi(MainWindow)
    MainWindow.center()
    select_ui(ui1)
    ui1.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
    ui1.graphicsView_2.setDragMode(QGraphicsView.ScrollHandDrag)

    '''各种功能-------------------------------------------------------------'''
    def openimage():
        """上传图片"""
        imgName, imgType = QFileDialog.getOpenFileName(
            None, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgName:
            print(imgName)
            global img_dir
            img_dir = imgName
            ui1.scene = QGraphicsScene()  # 创建场景
            img = QtGui.QPixmap(imgName)
            ui1.item = QGraphicsPixmapItem(img)
            ui1.scene.addItem(ui1.item)
            ui1.graphicsView.setScene(ui1.scene)

            ui1.graphicsView_2.setScene(ui1.scene)

    def punish():
        txt = ui1.lineEdit.text()
        matchObj = re.match(r'^[0-9]*$', txt, re.M | re.I)
        if matchObj:
            ui1.lineEdit.setText('成功！')
            img_analysis.punish(txt)
        else:
            ui1.lineEdit.setText('请输入数字！')

    '''连接各种功能-------------------------------------------------------------'''
    ui1.action1.triggered.connect(openimage)
    ui1.commitButton.clicked.connect(punish)


def open_boss():
    """打开项目负责人面板"""
    # 初始化
    thread1 = subthread.WeatherThread(converser)
    thread1.start()

    ui2 = ui_boss.Ui_BossWindow()
    ui2.setupUi(MainWindow)
    MainWindow.center()
    select_ui(ui2)
    ui2.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)

    '''各种功能-------------------------------------------------------------'''
    def openimage():
        """打开图片"""
        imgName, imgType = QFileDialog.getOpenFileName(
            None, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgName:
            print(imgName)
            global img_dir
            img_dir = imgName
            ui2.scene = QGraphicsScene()  # 创建场景
            img = QtGui.QPixmap(imgName)
            ui2.item = QGraphicsPixmapItem(img)
            ui2.scene.addItem(ui2.item)
            ui2.graphicsView.setScene(ui2.scene)

    def get_warning():
        decision.request_for_decision(converser)

    def submit():
        lenth = ui2.lineEdit.text()
        matchObj = re.match(r'^[0-9]*$', lenth, re.M | re.I)
        if matchObj:
            ui2.lineEdit.setText('')
            decision.make_announcement(int(lenth))
            ui2.label_13.setText('已发送')
        else:
            ui2.lineEdit.setText('')
            ui2.label_13.setText('请输入数字！')

    '''连接各种功能-------------------------------------------------------------'''
    ui2.ignoreButton.clicked.connect(lambda: ui2.label_13.setText('已忽略'))
    ui2.suspendButton.clicked.connect(submit)
    ui2.action2.triggered.connect(openimage)
    ui2.action1.triggered.connect(get_warning)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def center(self):
        """将本窗口移到中间"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    converser = params.Converser()

    app = QApplication(sys.argv)
    MainWindow = MyMainWindow()

    ui0 = ui_main.Ui_MainWindow()
    ui0.setupUi(MainWindow)
    MainWindow.show()

    ui0.btn_to_monitor.clicked.connect(open_monitor)
    ui0.btn_to_boss.clicked.connect(open_boss)

    sys.exit(app.exec_())
