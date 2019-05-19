# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/5/18 11:52'

import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QApplication, QDesktopWidget, QMainWindow
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sip


class UI_demo(QWidget):
    """用户界面"""
    def __init__(self):
        super().__init__()

        # 窗口信息
        self.title = 'PyQt5 demo'
        self.left = 600
        self.top = 200
        self.width = 800
        self.height = 600

        self.initUI()

    def initUI(self):

        # 窗口信息
        self.setWindowIcon(QIcon('./img/home.ico'))  # 图标设置
        self.setGeometry(self.left, self.top, self.width, self.height)  # 大小位置设置
        self.setWindowTitle(self.title)

        # # 窗口居中
        # self.resize(800, 600)  # 窗口大小
        # self.center()

        self.show()

        # # 计算按钮
        # cbtn = QPushButton('计算', self)
        # cbtn.setToolTip('计算下次定投金额')
        # cbtn.resize(100, 34)
        # cbtn.move(290, 550)
        #
        # # 图表按钮
        # ibtn = QPushButton('展示', self)
        # ibtn.setToolTip('展示图表')
        # ibtn.resize(100, 34)
        # ibtn.move(410, 550)
        #
        # exitAct = QAction(QIcon('./img/Agt Stop.ico'), '&Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Exit application')
        # exitAct.triggered.connect(qApp.quit)
        #
        # self.statusBar()
        #
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)
        #



    def center(self):
        """窗口居中"""

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = UI_demo()
    sys.exit(app.exec_())