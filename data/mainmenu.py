import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from data.titlebar import titlebar
from data.weather_forecast import XZS
from data.Calendar.QtUI import GUI
from data.home import home
from data.Loadapple import apple
from data.loadcherry import cherry
from data.loadcorn import corn
from data.loadgrape import grape
from data.loadcitrus import citrus
from data.loadpeachtwig import peachtwig
from data.loadcapsicum import capsicum
from data.loadpotato import potato
from data.loadstrawberry import strawberry
from data.loadtomato import tomato

class mainmenu(titlebar, QtWidgets.QMainWindow):
    def __init__(self):
        super(mainmenu, self).__init__()
        self.setupUi(self)

        self.Button_1.clicked.connect(self.bt_c1)
        self.Button_2.clicked.connect(self.bt_c2)
        self.Button_3.clicked.connect(self.bt_c3)
        self.Button_4.clicked.connect(self.bt_c4)#信号
        self.Button_5.clicked.connect(self.bt_c5)
        self.Button_6.clicked.connect(self.bt_c6)
        self.Button_7.clicked.connect(self.bt_c7)
        self.Button_8.clicked.connect(self.bt_c8)  # 信号
        self.Button_9.clicked.connect(self.bt_c9)
        self.Button_10.clicked.connect(self.bt_c10)
        self.Button_11.clicked.connect(self.bt_c11)
        self.Button_12.clicked.connect(self.bt_c12)  # 信号
        self.Button_13.clicked.connect(self.bt_c13)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(1520, 780)
        Form.setWindowTitle("农产测试助手")
        '''第一个按钮'''########################
        #字体样式
        font1 = QtGui.QFont()
        font1.setFamily('微软雅黑')
        font1.setBold(True)
        font1.setPointSize(18)
        font1.setWeight(50)
        #按钮美化
        self.Button_1 = QtWidgets.QPushButton(self)
        self.Button_1.setGeometry(QtCore.QRect(39, 47, 233, 80))
        self.Button_1.setObjectName("Button_1")
        self.Button_1.setText("首页")
        self.Button_1.setFont(font1)#继承了字体样式

        self.Button_1.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"#按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )
        '''第二个按钮'''####################
        self.Button_2 = QtWidgets.QPushButton(self)
        self.Button_2.setGeometry(QtCore.QRect(39, 570, 233, 80))
        font2 = QtGui.QFont()
        font2.setFamily('微软雅黑')
        font2.setBold(True)
        font2.setPointSize(18)
        font2.setWeight(50)
        self.Button_2.setFont(font2)
        self.Button_2.setObjectName("Button_2")
        self.Button_2.setText("天气查询")
        self.Button_2.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}" # 按钮背景
                                    #"QPushButton{color:white}" # 字体颜色
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )
        '''第三个按钮'''#######################
        font3 = QtGui.QFont()
        font3.setFamily('微软雅黑')
        font3.setBold(True)
        font3.setPointSize(18)
        font3.setWeight(50)
        self.Button_3 = QtWidgets.QPushButton(self)
        self.Button_3.setGeometry(QtCore.QRect(39, 670, 233, 80))
        self.Button_3.setObjectName("Button_3")
        self.Button_3.setText("万年历")
        self.Button_3.setFont(font3)
        self.Button_3.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"#按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第四个按钮'''  #######################苹果
        font3 = QtGui.QFont()
        font3.setFamily('微软雅黑')
        font3.setBold(True)
        font3.setPointSize(18)
        font3.setWeight(50)
        self.Button_4 = QtWidgets.QPushButton(self)
        self.Button_4.setGeometry(QtCore.QRect(39, 207, 100, 60))
        self.Button_4.setObjectName("Button_3")
        self.Button_4.setText("苹果")
        self.Button_4.setFont(font3)
        self.Button_4.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第5个按钮'''  #######################樱桃
        self.Button_5 = QtWidgets.QPushButton(self)
        self.Button_5.setGeometry(QtCore.QRect(172, 207, 100, 60))
        self.Button_5.setObjectName("Button_3")
        self.Button_5.setText("樱桃")
        self.Button_5.setFont(font3)
        self.Button_5.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第6个按钮'''  #######################玉米
        self.Button_6 = QtWidgets.QPushButton(self)
        self.Button_6.setGeometry(QtCore.QRect(39, 277, 100, 60))
        self.Button_6.setObjectName("Button_3")
        self.Button_6.setText("玉米")
        self.Button_6.setFont(font3)
        self.Button_6.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第7个按钮'''  #######################葡萄
        self.Button_7 = QtWidgets.QPushButton(self)
        self.Button_7.setGeometry(QtCore.QRect(172, 277, 100, 60))
        self.Button_7.setObjectName("Button_3")
        self.Button_7.setText("葡萄")
        self.Button_7.setFont(font3)
        self.Button_7.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第8个按钮'''  #######################柑桔
        self.Button_8 = QtWidgets.QPushButton(self)
        self.Button_8.setGeometry(QtCore.QRect(39, 347, 100, 60))
        self.Button_8.setObjectName("Button_3")
        self.Button_8.setText("柑桔")
        self.Button_8.setFont(font3)
        self.Button_8.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第9个按钮'''  #######################桃子
        self.Button_9 = QtWidgets.QPushButton(self)
        self.Button_9.setGeometry(QtCore.QRect(172, 347, 100, 60))
        self.Button_9.setObjectName("Button_3")
        self.Button_9.setText("桃子")
        self.Button_9.setFont(font3)
        self.Button_9.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第10个按钮'''  #######################辣椒
        self.Button_10 = QtWidgets.QPushButton(self)
        self.Button_10.setGeometry(QtCore.QRect(39, 417, 100, 60))
        self.Button_10.setObjectName("Button_3")
        self.Button_10.setText("辣椒")
        self.Button_10.setFont(font3)
        self.Button_10.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第11个按钮'''  #######################马铃薯
        self.Button_11 = QtWidgets.QPushButton(self)
        self.Button_11.setGeometry(QtCore.QRect(172, 417, 100, 60))
        self.Button_11.setObjectName("Button_3")
        self.Button_11.setText("马铃薯")
        self.Button_11.setFont(font3)
        self.Button_11.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第12个按钮'''  #######################草莓
        self.Button_12 = QtWidgets.QPushButton(self)
        self.Button_12.setGeometry(QtCore.QRect(39, 487, 100, 60))
        self.Button_12.setObjectName("Button_3")
        self.Button_12.setText("草莓")
        self.Button_12.setFont(font3)
        self.Button_12.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第13个按钮'''  #######################番茄
        self.Button_13 = QtWidgets.QPushButton(self)
        self.Button_13.setGeometry(QtCore.QRect(172, 487, 100, 60))
        self.Button_13.setObjectName("Button_3")
        self.Button_13.setText("番茄")
        self.Button_13.setFont(font3)
        self.Button_13.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )

        '''第14个按钮'''  #######################农作物病虫害检测
        self.Button_14 = QtWidgets.QPushButton(self)
        self.Button_14.setGeometry(QtCore.QRect(39, 137, 233, 60))
        self.Button_14.setObjectName("Button_3")
        self.Button_14.setText("农作物病害检测")
        self.Button_14.setFont(font3)
        self.Button_14.setStyleSheet("QPushButton{border-image: url(image/btn5.jpg)}"  # 按钮背景
                                    "QPushButton{border-radius:6px}"  # 圆角半径
                                    )




        """右侧总框架"""
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(300, 37, 1211, 734))
        #self.stackedWidget.setStyleSheet("background-color: blue;")
        self.stackedWidget.setObjectName("stackedWidget")
        '''第一页'''#首页
        self.page_1 = home()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        '''第二页'''#天气查询
        self.page_2 = XZS()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        '''第三页'''#万年历
        self.page_3 = GUI()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        '''第四页'''#苹果
        self.page_4 = apple()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        '''第5页'''  # 樱桃
        self.page_5 = cherry()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        '''第6页'''  # 玉米
        self.page_6 = corn()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        '''第7页'''  # 葡萄
        self.page_7 = grape()
        self.page_7.setObjectName("page_7")
        self.stackedWidget.addWidget(self.page_7)
        '''第8页'''#柑桔
        self.page_8 = citrus()
        self.page_8.setObjectName("page_8")
        self.stackedWidget.addWidget(self.page_8)
        '''第9页'''  # 桃子
        self.page_9 = peachtwig()
        self.page_9.setObjectName("page_9")
        self.stackedWidget.addWidget(self.page_9)
        '''第10页'''  # 辣椒
        self.page_10 = capsicum()
        self.page_10.setObjectName("page_10")
        self.stackedWidget.addWidget(self.page_10)
        '''第11页'''  # 马铃薯
        self.page_11 = potato()
        self.page_11.setObjectName("page_11")
        self.stackedWidget.addWidget(self.page_11)
        '''第12页'''  # 草莓
        self.page_12 = strawberry()
        self.page_12.setObjectName("page_12")
        self.stackedWidget.addWidget(self.page_12)
        '''第13页'''  # 番茄
        self.page_13 = tomato()
        self.page_13.setObjectName("page_13")
        self.stackedWidget.addWidget(self.page_13)

        self.stackedWidget.setCurrentIndex(0)  # 初始界面索引为0

    def bt_c1(self):  # 按钮连接
        self.stackedWidget.setCurrentIndex(0)

    def bt_c2(self):
        self.stackedWidget.setCurrentIndex(1)

    def bt_c3(self):
        self.stackedWidget.setCurrentIndex(2)

    def bt_c4(self):
        self.stackedWidget.setCurrentIndex(3)

    def bt_c5(self):  # 按钮连接
        self.stackedWidget.setCurrentIndex(4)

    def bt_c6(self):
        self.stackedWidget.setCurrentIndex(5)

    def bt_c7(self):
        self.stackedWidget.setCurrentIndex(6)

    def bt_c8(self):
        self.stackedWidget.setCurrentIndex(7)

    def bt_c9(self):  # 按钮连接
        self.stackedWidget.setCurrentIndex(8)

    def bt_c10(self):
        self.stackedWidget.setCurrentIndex(9)

    def bt_c11(self):
        self.stackedWidget.setCurrentIndex(10)

    def bt_c12(self):
        self.stackedWidget.setCurrentIndex(11)

    def bt_c13(self):
        self.stackedWidget.setCurrentIndex(12)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = mainmenu()
    demo.show()
    sys.exit(app.exec_())