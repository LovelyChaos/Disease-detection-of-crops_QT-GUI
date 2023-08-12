'''查询天气'''
import sys
import urllib
from json import JSONDecodeError
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class XZS(QWidget):
    def __init__(self):
        super(XZS, self).__init__()

        self.resize(1211, 734)
        ###

        font = QtGui.QFont()
        font.setFamily("宋体")

        self.label1 = QLabel(self)
        self.label1.setFont(font)
        self.label1.setText("请输入查询地所在城市")
        # self.label1.setFixedSize(300, 400)
        self.label1.move(60, 30)

        self.textEdit = QLineEdit(self)
        self.textEdit.move(60, 50)
        self.textEdit.setFont(font)

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.move(650, 30)
        self.textEdit2.setFixedSize(500, 180)
        self.textEdit2.setStyleSheet(
                      "QTextEdit{background-attachment:fixed;\n}"
                      "QTextEdit{background-repeat:none;\n}"
                      "QTextEdit{background-position:center}"
                      "QTextEdit{border-image: url(image/btn4.jpg)}"
                      "QTextEdit{border-radius:9px}"  # 圆角
        )

        self.textEdit2.setFont(font)
        self.textEdit2.setFocusPolicy(QtCore.Qt.NoFocus)



        btn_1 = QPushButton(self)
        btn_1.setText("查询")
        btn_1.move(60, 120)
        btn_1.setFixedSize(100, 50)
        btn_1.setStyleSheet(
            "QPushButton{border-radius:9px}"  # 圆角
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{border-image: url(image/btn5.jpg)}")
        btn_1.clicked.connect(self.look)




    ###设置大背景
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("image/wf1.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)


    def look(self):
        city = self.textEdit.text()
        print(city)

        html = f'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city)

        try:
            info = requests.get(html)
            # print(info)
            info.encoding = 'utf-8'
        except requests.ConnectionError:
            raise

        try:
            info_json = info.json()
            # print(info_json)
        except JSONDecodeError:
            return '无法查询'

        try:
            for i in range(1):  # 将每一天的数据放入列表中
                # 天气情况
                data = info_json['data']
                city = f" 城市：{data['city']}\n"
                # 以 f开头表示在字符串内支持大括号内的python 表达式
                today = data['forecast'][i]
                date = f" 日期：{today['date']}\n"
                now = f" 实时温度：{data['wendu']}度\n"
                temperature = f" 温度：{today['high']} {today['low']}\n"
                fengxiang = f" 风向：{today['fengxiang']}\n"
                type = f" 天气：{today['type']}\n"
                tips = f" 贴士：{data['ganmao']}\n"

                self.textEdit2.setText(city + date + now + temperature + fengxiang + type + tips + "\n\n")
                #print(city + date + now + temperature + fengxiang + type + tips + "\n\n")

                self.textEdit.clear()

        except:
            self.textEdit2.setText('请输入正确的城市名称')
            self.textEdit.clear()


    def keyPressEvent(self,e):
        # 设置快捷键
        if e.key() == Qt.Key_Return:
                self.look()
        # if event.key() == QtCore.Qt.Key_Escape:  # 当我们按住键盘是esc按键时
        #     self.close()  # 关闭程序



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = XZS()
    my.show()
    sys.exit(app.exec_())

