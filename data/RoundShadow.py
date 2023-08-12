'''
圆角和阴影和背景图 最初的类
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
class RoundShadow(QWidget):
    """圆角边框类"""

    def __init__(self, parent=None):
        super(RoundShadow, self).__init__(parent)
        self.border_width = 8
        # 设置 窗口无边框和背景透明 *必须
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.resize(1520, 780)


    def paintEvent(self, event):
        # 阴影
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)

        pat = QPainter(self)
        pat.setRenderHint(pat.Antialiasing)
        pat.fillPath(path, QBrush(Qt.white))

        color = QColor(0, 0, 0, 100) #阴影颜色

        for i in range(10):
            i_path = QPainterPath()
            i_path.setFillRule(Qt.WindingFill)
            ref = QRectF(10 - i, 10 - i, self.width() - (10 - i) * 2, self.height() - (10 - i) * 2)
            # i_path.addRect(ref)
            i_path.addRoundedRect(ref, self.border_width, self.border_width)
            color.setAlpha(150 - i ** 0.5 * 50)
            pat.setPen(color)
            pat.drawPath(i_path)

        # 圆角
        pat2 = QPainter(self)
        pat2.setRenderHint(pat2.Antialiasing)  # 抗锯齿
        #pat2.setBrush(Qt.blue)
        pat2.setPen(Qt.transparent)

        rect = self.rect()
        rect.setLeft(9)
        rect.setTop(9)
        rect.setWidth(rect.width() - 9)
        rect.setHeight(rect.height() - 9)
        pat2.drawRoundedRect(rect, 4, 4)

    #####窗口可移动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))




class BackImg(QMainWindow):
    def __init__(self, parent=None):
        super(BackImg, self).__init__(parent)

        self.resize(1520, 780)
        self.bg_color = QColor(255, 255, 255)

    def paintEvent(self, e):
        super(BackImg, self).paintEvent(e)
        pat = QPainter(self)
        pat.setPen(Qt.NoPen)

        brush = QBrush()

        brush.setTextureImage(QImage("image/image2.jpg"))
        pat.setBrush(brush)

        rect = self.rect()

        rect.setLeft(9)
        rect.setTop(9)
        rect.setWidth(rect.width() - 9)
        rect.setHeight(rect.height() - 9)

        pat.drawRoundedRect(rect, 4, 4)


class TestWindow(RoundShadow, QWidget):
    """测试窗口"""

    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)

        self.resize(1520, 780)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = TestWindow()
    t.show()
    app.exec_()
