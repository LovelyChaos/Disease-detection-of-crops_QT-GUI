import sys
from PyQt5.QtWidgets import QApplication
from data.mainmenu import mainmenu
if __name__ == '__main__':
    app = QApplication(sys.argv) #启动
    Mainmenu = mainmenu()
    Mainmenu.show() #显示主菜单
    sys.exit(app.exec_())#退出