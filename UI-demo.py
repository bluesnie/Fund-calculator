# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/5/18 11:52'

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget, QMainWindow, QComboBox, QTabWidget, \
    QHBoxLayout, QGridLayout, QCalendarWidget
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QLineEdit, QVBoxLayout, QLabel, QGroupBox, QCheckBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDialogButtonBox, QSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sip


class Window(QWidget):
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
        # self.setGeometry(self.left, self.top, self.width, self.height)  # 大小位置设置
        self.setWindowTitle(self.title)

        # 窗口居中
        self.resize(self.width, self.height)  # 窗口大小
        self.center()

        # 选项卡
        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        # 按钮
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # buttonbox.accepted.connect(self.accept)
        # buttonbox.accepted.connect(self.reject)
        # 选项卡
        tabWidget.addTab(Income(), "收入")
        tabWidget.addTab(Expenditure(), '支出')

        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.show()

    def center(self):
        """窗口居中"""

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Income(QWidget):
    """收入选项卡"""
    def __init__(self):
        super().__init__()

        nameLabel = QLabel("Name: ")
        nameEdit = QLineEdit()

        phoneLabel = QLabel("Phone: ")
        phoneEdit = QLineEdit()

        emailLabel = QLabel("Email: ")
        emailEdit = QLineEdit()

        vbox = QVBoxLayout()

        vbox.addWidget(nameLabel)
        vbox.addWidget(nameEdit)

        vbox.addWidget(phoneLabel)
        vbox.addWidget(phoneEdit)

        vbox.addWidget(emailLabel)
        vbox.addWidget(emailEdit)

        self.setLayout(vbox)


class Expenditure(QWidget):
    """支出选项卡"""
    def __init__(self):
        super().__init__()

        self.typeLabel = QLabel("分类: ")
        self.accountLabel = QLabel("账户: ")
        self.moneyLabel = QLabel("金额: ")
        self.memberLabel = QLabel("成员：")
        self.timeLabel = QLabel("时间：")
        self.commentLabel = QLabel("备注：")

        self.list1 = ["日常购物", '衣服饰品', '食品酒水', '居家物业']
        self.list2 = ['现金', '银行卡', '支付宝']
        self.list3 = ["本人", '老公', '老婆', '子女', '父母']

        self.moneyLineedit = QLineEdit()
        self.timeLineedit = QLineEdit()
        self.commentLineedit = QLineEdit()

        self.createExpenditureBox()
        self.Calender()
        self.groupBox2.setVisible(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.groupBox2)
        self.setLayout(vbox)

    def createExpenditureBox(self):
        combo = QComboBox()
        combo.addItems(self.list1)

        combo2 = QComboBox()
        combo2.addItems(self.list2)

        combo3 = QComboBox()
        combo3.addItems(self.list3)

        self.groupBox = QGroupBox('支出', alignment=Qt.AlignCenter)
        gridLayout = QGridLayout()

        gridLayout.addWidget(self.typeLabel, 0, 0)
        gridLayout.addWidget(combo, 0, 1)
        gridLayout.addWidget(self.accountLabel, 0, 2)
        gridLayout.addWidget(combo2, 0, 3)
        gridLayout.addWidget(self.moneyLabel, 0, 4)
        gridLayout.addWidget(self.moneyLineedit, 0, 5)

        gridLayout.addWidget(self.memberLabel, 1, 0)
        gridLayout.addWidget(combo3, 1, 1)
        gridLayout.addWidget(self.timeLabel, 1, 2)
        gridLayout.addWidget(self.timeLineedit, 1, 3)
        gridLayout.addWidget(self.commentLabel, 1, 4)
        gridLayout.addWidget(self.commentLineedit, 1, 5)

        btn = QPushButton('选择时间')
        btn.clicked.connect(self.CalenderIsVisibled)
        gridLayout.addWidget(btn, 3, 3)
        self.groupBox.setLayout(gridLayout)

    def Calender(self):
        """日历"""
        self.groupBox2 = QGroupBox("日历", alignment=Qt.AlignCenter)
        vbox = QVBoxLayout()
        self.calender = QCalendarWidget()
        self.calender.selectionChanged.connect(self.onSelectionChanged)
        self.calender.setGridVisible(True)
        vbox.addWidget(self.calender)
        self.groupBox2.setLayout(vbox)

    def onSelectionChanged(self):
        ca = self.calender.selectedDate()
        self.timeLineedit.setText(ca.toString(Qt.ISODate))

    def CalenderIsVisibled(self):
        """日历是否可见"""
        if self.groupBox2.isVisible():
            self.groupBox2.setVisible(False)
        else:
            self.groupBox2.setVisible(True)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())