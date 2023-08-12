'''打开电脑图片并显示'''
import sys, os
from Program.test import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def font(text, size=12, color="gray", bold="normal"):
    text = "<font style='font-size:" + str(size) + \
           "px; text-align:center; color:" + color + ";font-weight:" + \
           str(bold) + ";'>" + str(text) + "</font><br/>"
    return text


class corn(QMainWindow):
    def __init__(self):
        super(corn, self).__init__()
        ##显示图片#######
        self.resize(600, 400)

        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)
        self.label.move(600, 40)
        font2 = QtGui.QFont()
        font2.setFamily('微软雅黑')
        font2.setBold(True)
        font2.setPointSize(36)
        font2.setWeight(50)
        self.label.setFont(font2)
        self.label.setText("     显示图片")
        self.label.setStyleSheet("QLabel{border-image: url(image/btn8.jpg)}"  # 设置label的背景图片，设置后一直存在
                                 "QLabel{color:rgb(300,300,300,120)}"
                                 )
        ######打开图片###
        btn = QPushButton(self)
        btn.setText("打开图片")
        font2 = QtGui.QFont()
        font2.setFamily('微软雅黑')
        font2.setBold(True)
        font2.setPointSize(18)
        font2.setWeight(50)
        btn.setFont(font2)
        btn.setObjectName("Button_2")
        btn.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                          "QPushButton{border-radius:6px}"  # 圆角半径
                          )
        btn.setGeometry(QtCore.QRect(160, 40, 233, 80))
        btn.clicked.connect(self.openimage)

        ####解释框
        self.label2 = QLabel(self)
        self.label2.setFixedSize(400, 300)
        self.label2.move(160, 140)
        font2 = QtGui.QFont()
        font2.setFamily('微软雅黑')
        font2.setBold(True)
        font2.setPointSize(18)
        font2.setWeight(50)
        self.label2.setFont(font2)
        self.label2.setText("请从您的电脑上打开一张<br/>玉米的叶片图像")
        self.label2.setAlignment(Qt.AlignVCenter)
        self.label2.setStyleSheet("QLabel{border-image: url(image/btn8.jpg)}"  # 设置label的背景图片，设置后一直存在
                                  "QLabel{border-radius:9px}"  # 圆角
                                  )

        ####输出病变的label####
        font1 = QtGui.QFont()
        font1.setFamily("微软雅黑")
        font1.setPointSize(20)
        self.textEdit2 = QTextEdit(self)
        self.textEdit2.move(160, 550)
        self.textEdit2.setFixedSize(840, 100)
        self.textEdit2.setStyleSheet(
            "QTextEdit{background-attachment:fixed;\n}"
            "QTextEdit{background-repeat:none;\n}"
            "QTextEdit{background-position:center}"
            "QTextEdit{border-image: url(image/btn9.jpg)}"
            "QTextEdit{border-radius:9px}"  # 圆角
        )
        self.textEdit2.setFont(font1)
        self.textEdit2.setFocusPolicy(QtCore.Qt.NoFocus)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("image/corn.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")  # 在电脑上加代码
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        print("imgName", imgName)
        self.label.setPixmap(jpg)
        model_dir = '2018-11-04_acc_best.pth'
        # model_dir = 'D:/Dachuang/APP/2018-11-04_acc_best.pth'
        print(os.path.isfile(model_dir))
        final_label = predict(imgName, model_dir)
        print('final_label: ', final_label)
        if final_label == 9:
            self.textEdit2.setText("玉米健康")
        elif final_label == 10:
            self.textEdit2.setText("玉米灰斑病一般")
        elif final_label == 11:
            self.textEdit2.setText("玉米灰斑病严重")
        elif final_label == 12:
            self.textEdit2.setText("玉米锈病一般")
        elif final_label == 13:
            self.textEdit2.setText("玉米锈病严重")
        elif final_label == 14:
            self.textEdit2.setText("玉米叶斑病一般")
        elif final_label == 15:
            self.textEdit2.setText("玉米叶斑病严重")
        elif final_label == 16:
            self.textEdit2.setText("玉米花叶病毒病")
        else:
            self.textEdit2.setText("请放入正确的图像！！！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = apple()
    my.show()
    sys.exit(app.exec_())
