# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/5/19 11:49'

# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/5/18 11:52'

import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QApplication, QDesktopWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout, QRadioButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5 import QtGui
import sip


class UI_demo(QDialog):
    """用户界面"""
    def __init__(self):
        super().__init__()

        # 窗口信息
        self.title = 'PyQt5 demo'
        self.left = 600
        self.top = 200
        self.width = 800
        self.height = 600

        self.initWindow()

    def initWindow(self):

        # 窗口信息
        self.setWindowIcon(QtGui.QIcon('./img/home.ico'))  # 图标设置
        # self.setGeometry(self.left, self.top, self.width, self.height)  # 大小位置设置
        self.setWindowTitle(self.title)  # 窗口标题
        self.resize(800, 600)  # 窗口大小
        self.center()        # 窗口居中

        # 按钮
        # self.button1()

        # 布局
        # self.createLayout()
        # vbox = QVBoxLayout()
        # vbox.addWidget(self.groupBox)

        # # 标签
        # label = QLabel('This is Label.')
        # vbox.addWidget(label)
        #
        # label2 = QLabel('This is Label.')
        # label2.setFont(QtGui.QFont("Sanserif", 20))  # 设置字体和大小
        # label2.setStyleSheet("color:red")  # 设置颜色
        # vbox.addWidget(label2)
        #
        # # 背景图
        # labelImage = QLabel(self)
        # pixmap = QtGui.QPixmap('./img/home')
        # labelImage.setPixmap(pixmap)
        # vbox.addWidget(labelImage)

        # self.setLayout(vbox)

        # 单选按钮
        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("sanserif", 12))
        vbox.addWidget(self.label)

        self.setLayout(vbox)



        # 展示窗口
        self.show()

    def button1(self):
        """按钮1"""
        btn = QPushButton('click me', self)
        # btn.resize(100, 34) # 按钮大小
        # btn.move(290, 550)  # 移动按钮
        # 合并
        btn.setGeometry(QtCore.QRect(290, 550, 100, 34))
        # 按钮图标
        btn.setIcon(QtGui.QIcon('./img/home.ico'))
        btn.setIconSize(QtCore.QSize(40,40))  # 设置图标大小
        # 设置按钮提示
        btn.setToolTip('按钮提示')
        # 触发事件
        btn.clicked.connect(self.ClickMe)

    def ClickMe(self):
        print('Hello World')
        # 退出
        sys.exit()

    def center(self):
        """窗口居中"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def createLayout(self):
    #     """布局"""
    #     self.groupBox = QGroupBox('Whick one?')
    #     # 第一种布局
    #     # hboxlayout = QHBoxLayout()
    #     #
    #     # btn = QPushButton('One', self)
    #     # btn.setIcon(QtGui.QIcon('./img/home.ico'))
    #     # btn.setIconSize(QtCore.QSize(40, 40))
    #     # btn.setMinimumHeight((40))
    #     # hboxlayout.addWidget(btn)
    #     #
    #     # btn1 = QPushButton('Two', self)
    #     # btn1.setIcon(QtGui.QIcon('./img/home.ico'))
    #     # btn1.setIconSize(QtCore.QSize(40, 40))
    #     # btn1.setMinimumHeight((40))
    #     # hboxlayout.addWidget(btn1)
    #     #
    #     # btn2 = QPushButton('Three', self)
    #     # btn2.setIcon(QtGui.QIcon('./img/home.ico'))
    #     # btn2.setIconSize(QtCore.QSize(40, 40))
    #     # btn2.setMinimumHeight((40))
    #     # hboxlayout.addWidget(btn2)
    #     # self.groupBox.setLayout(hboxlayout)
    #     # 第二种布局
    #     gridLayout = QGridLayout()
    #     btn = QPushButton('Python', self)
    #     btn.setIcon(QtGui.QIcon('./img/home.ico'))
    #     btn.setIconSize(QtCore.QSize(40, 40))
    #     btn.setMinimumHeight((40))
    #     gridLayout.addWidget(btn, 0, 0)
    #
    #     btn1 = QPushButton('java', self)
    #     btn1.setIcon(QtGui.QIcon('./img/home.ico'))
    #     btn1.setIconSize(QtCore.QSize(40, 40))
    #     btn1.setMinimumHeight((40))
    #     gridLayout.addWidget(btn1, 0, 1)
    #
    #     btn2 = QPushButton('php', self)
    #     btn2.setIcon(QtGui.QIcon('./img/home.ico'))
    #     btn2.setIconSize(QtCore.QSize(40, 40))
    #     btn2.setMinimumHeight((40))
    #     gridLayout.addWidget(btn2, 1, 0)
    #
    #     btn3 = QPushButton('c++', self)
    #     btn3.setIcon(QtGui.QIcon('./img/home.ico'))
    #     btn3.setIconSize(QtCore.QSize(40, 40))
    #     btn3.setMinimumHeight((40))
    #     gridLayout.addWidget(btn3, 1, 1)
    #     self.groupBox.setLayout(gridLayout)

    def radioButton(self):
        """单选按钮"""
        self.groupBox = QGroupBox("radio button")
        self.groupBox.setFont(QtGui.QFont("sanserif", 12))
        hboxlayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton('one')
        self.radiobtn1.setChecked(True)  # 选中状态
        self.radiobtn1.setIcon(QtGui.QIcon('./img/home.ico'))
        self.radiobtn1.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn1.setFont(QtGui.QFont('sanserif', 13))
        self.radiobtn1.toggled.connect(self.OnRadioBtn)  # 选中事件
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton('two')
        self.radiobtn2.setIcon(QtGui.QIcon('./img/home.ico'))
        self.radiobtn2.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn2.setFont(QtGui.QFont('sanserif', 13))
        self.radiobtn2.toggled.connect(self.OnRadioBtn)
        hboxlayout.addWidget(self.radiobtn2)

        self.groupBox.setLayout(hboxlayout)

    def OnRadioBtn(self):
        """单选框选中事件"""
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You have selected " + radioBtn.text())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = UI_demo()
    sys.exit(app.exec_())
