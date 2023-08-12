'''首页'''
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
def font(text, size=12, color="gray", bold="normal"):
	text = "<font style='font-size:" + str(size) +\
           "px; text-align:center; color:" + color + ";font-weight:" + \
           str(bold) + ";'>" + str(text) + "</font><br/>"
	return text
class home(QWidget):
    def __init__(self):
        super(home, self).__init__()

        self.resize(1211, 734)
        ###

        font1 = QtGui.QFont()
        font1.setFamily("宋体")

        ####logo的label
        self.label1 = QLabel(self)
        self.label1.setFont(font1)
        #self.label1.setText("请输入查询地所在城市")
        self.label1.setStyleSheet(
            "QLabel{border-image: url(image/logo.png)}"  # 设置label的背景图片，设置后一直存在
            "QLabel{border-radius:9px}"  # 圆角
        )
        self.label1.setFixedSize(100, 100)
        self.label1.move(540, 43)

        ####农产测试助手
        font2 = QtGui.QFont()
        font2.setFamily('微软雅黑')
        font2.setBold(True)
        font2.setPointSize(18)
        font2.setWeight(50)
        self.label2 = QLabel(self)

        self.label2.setFont(font2)
        #self.label2.setText("农产测试助手")
        self.label2.setFont(font1)
        self.label2.setStyleSheet(
            # "QLabel{border-image: url(image/logo.png)}"  # 设置label的背景图片，设置后一直存在
            "QLabel{border-radius:9px}"  # 圆角
        )
        self.label2.setFixedSize(200, 50)
        self.label2.move(69, 230)


        ####信息
        self.label3 = QLabel(self)
        self.label3.setGeometry(QtCore.QRect(350, 15, 480, 700))
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label3.setStyleSheet(
            "QLabel{border-image: url(image/biankuang2.jpg)}"  # 设置label的背景图片，设置后一直存在
            "QLabel{border-radius:9px}"  # 圆角
        )
        self.label3.setText(
            "<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>"
            "<br/><br/>{}<br/>{}<br/>{}<br/>{}".format(
                font('农产测试助手', 45, "black"),
                font('专业团队', 36, "black"),
                font('哈尔滨职业技术学院', 44, "black"),
                font('智能控制实验室', 24, "black")))
        self.label3.lower()

    ###设置大背景
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("image/image6.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)