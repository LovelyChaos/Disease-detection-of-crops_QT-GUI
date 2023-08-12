'''自定义工具栏 logo 左侧导航栏背景'''
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QHBoxLayout, QLabel, QGraphicsLineItem
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from data.RoundShadow import RoundShadow, QPainter, QPen
from PyQt5.QtCore import Qt
class titlebar(RoundShadow, QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('image/logo.png'))
        #####最小化按钮
        self.min_Button = QPushButton(self)  # 定义一个按钮
        self.min_Button.setGeometry(QtCore.QRect(1450, 10, 25, 25))  # 按钮左边，上边，宽度和高度
        self.min_Button.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{border-image: url(image/minwindow.png)}"  # 设置按钮的背景图片，设置后一直存在
                                        "QPushButton{border-radius:3px}"  # 圆角
                                        )  # 美化按钮
        self.min_Button.clicked.connect(self.showMinimized)  # 最小化按钮

        #####关闭窗口按钮
        self.close_Button = QPushButton(self)  # 定义一个按钮
        self.close_Button.setGeometry(QtCore.QRect(1480, 10, 25, 25))  # 按钮左边，上边，宽度和高度
        self.close_Button.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{border-image: url(image/closewindow.ico)}"  # 设置按钮的背景图片，设置后一直存在
                                        "QPushButton{border-radius:3px}"  # 圆角
                                        )  # 美化按钮
        self.close_Button.clicked.connect(self.close)  # 关闭窗口按钮

        #####logo label
        self.logo_label = QLabel(self)
        self.logo_label.setFixedSize(25, 25)
        self.logo_label.move(10, 10)
        self.logo_label.setStyleSheet(
                                      "QLabel{border-image: url(image/logo.png)}"  # 设置label的背景图片，设置后一直存在
                                 )

        #####美化工具栏
        self.titlebar_label = QLabel(self)
        self.titlebar_label.setFixedSize(1502, 28)
        self.titlebar_label.move(9, 9)
        self.titlebar_label.setStyleSheet(
            "QLabel{border-image: url(image/titlebar.png)}"  # 设置label的背景图片，设置后一直存在
        )
        self.titlebar_label.lower()

        #####左侧背景
        self.left_background_label = QLabel(self)
        self.left_background_label.setFixedSize(293, 734)
        self.left_background_label.move(9, 37)
        self.left_background_label.setStyleSheet(
            "QLabel{border-image: url(image/left.jpg)}"  # 设置label的背景图片，设置后一直存在
        )
        self.left_background_label.lower()







