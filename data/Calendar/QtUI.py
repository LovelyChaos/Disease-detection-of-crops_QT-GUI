from data.Calendar.CustomizeWidgets import *
from data.Calendar.PerpetualCalendar import *
class GUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.wnlWidget = QWidget()

		self.setupUI()

	def setupUI(self):
		pe = QPalette()
		pe.setColor(QPalette.Window, QColor(250, 255, 0))  # F0FFFF、FFFAFA、FFFAF0
		self.setPalette(pe)
		self.setFixedSize(1211, 734)
		#self.setWindowTitle("万年历")
		self.setCentralWidget(self.wnlWidget)
		self.calendarUI()
		displayDate(self)
		self.show()

	def paintEvent(self, event):
		painter = QPainter(self)
		pixmap = QPixmap("image/calendar.jpg")
		# 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
		painter.drawPixmap(self.rect(), pixmap)



	def calendarUI(self):
		self.gridWNL = QGridLayout()
		self.wnlWidget.setLayout(self.gridWNL)
		self.gridWNL.setSpacing(0)
		self.hlayWNL = QHBoxLayout()#水平布局
		self.hlayWNL.setContentsMargins(0, 0, 0, 0)#左、上、右、下的外边距
		self.gridWNL.addLayout(self.hlayWNL, 0, 0, 1, 7)
		self.cblCentury = ComboBox()
		for i in range(startCentury, endCentury+1):
			if i < 0: self.cblCentury.addItem('BC' + str(abs(i)) + '世纪')
			elif i == 0: continue
			else: self.cblCentury.addItem(str(i) + '世纪')
		self.cblCentury.currentIndexChanged.connect(lambda : yearItems(self))
		self.cblCentury.activated.connect(lambda : displayDate(self))
		self.cblCentury.setMaximumWidth(80)
		self.cblCentury.setMaximumHeight(150)
		self.cblCentury.setFocusPolicy(False)
		self.cblCentury.setStyleSheet("QComboBox{background:#F7D674}")
		self.hlayWNL.addWidget(self.cblCentury)#添加世纪控件
		self.cblYear = ComboBox()
		self.cblYear.setFixedWidth(82)
		self.cblYear.setMaximumHeight(150)
		self.cblYear.setStyleSheet("QComboBox{background:#F7D674}")
		self.btnLastYear = QPushButton('<')
		self.btnNextYear = QPushButton('>')
		self.cblYear.activated.connect(lambda : displayDate(self))
		self.cblYear.wheeled.connect(lambda :jumpYear(self))
		self.btnLastYear.clicked.connect(self.thisJumpMonth)
		self.btnNextYear.clicked.connect(self.thisJumpMonth)
		self.btnLastYear.setMaximumSize(16, 150)
		self.btnNextYear.setMaximumSize(16, 150)
		self.btnLastYear.setStyleSheet(
			'''QPushButton{background:#F7D674;}
            QPushButton:hover{background:yellow;}''')
		self.btnNextYear.setStyleSheet(
			'''QPushButton{background:#F7D674;}
            QPushButton:hover{background:yellow;}''')

		self.hlayWNL.addStretch()
		self.hlayWNL.addWidget(self.btnLastYear)
		self.hlayWNL.addWidget(self.cblYear)
		self.hlayWNL.addWidget(self.btnNextYear)#添加控件
		self.cblMonth = ComboBox()
		for i in range(12):
			self.cblMonth.addItem(str(i + 1) + '月')
		self.cblMonth.setMaxVisibleItems(12)
		self.cblMonth.setFocusPolicy(False)
		self.cblMonth.setMaximumWidth(80)
		self.cblMonth.setMaximumHeight(150)
		self.btnLastMonth = QPushButton("<")
		self.btnNextMonth = QPushButton(">")
		self.btnLastMonth.setStyleSheet(
			'''QPushButton{background:#F7D674;}
            QPushButton:hover{background:yellow;}''')
		self.btnNextMonth.setStyleSheet(
			'''QPushButton{background:#F7D674;}
            QPushButton:hover{background:yellow;}''')
		self.cblMonth.activated.connect(lambda : displayDate(self))
		self.cblMonth.wheeled.connect(lambda :jumpMonth(self))
		self.cblMonth.setStyleSheet("QComboBox{background:#F7D674}")
		self.btnLastMonth.clicked.connect(self.thisJumpMonth)
		self.btnNextMonth.clicked.connect(self.thisJumpMonth)
		self.btnLastMonth.setMaximumSize(16, 150)
		self.btnNextMonth.setMaximumSize(16, 150)
		self.hlayWNL.addStretch()
		self.hlayWNL.addWidget(self.btnLastMonth)
		self.hlayWNL.addWidget(self.cblMonth)
		self.hlayWNL.addWidget(self.btnNextMonth)
		self.hlayWNL.addStretch()
		self.btnToday = QPushButton("今日")
		self.btnToday.clicked.connect(lambda : displayDate(self))
		self.btnToday.setStyleSheet(
			'''QPushButton{background:#F7D674;}
			QPushButton:hover{background:yellow;}''')
		self.btnToday.setMaximumWidth(500)
		self.hlayWNL.addWidget(self.btnToday)
		self.labMonday = Label("一")
		self.labTuesday = Label("二")
		self.labWednesday = Label("三")
		self.labThursday = Label("四")
		self.labFriday = Label("五")
		self.labSaturday = Label("六")
		self.labSunday = Label("日")
		labWeeks = [self.labMonday, self.labTuesday, self.labWednesday, self.labThursday, self.labFriday, self.labSaturday, self.labSunday]
		for i in range(7):
			self.gridWNL.addWidget(labWeeks[i], 1, i)
			labWeeks[i].setMaximumHeight(40)
		self.lab00, self.lab01, self.lab02, self.lab03, self.lab04, self.lab05, self.lab06 = Label(), Label(), Label(), Label(), Label(), Label(), Label()
		self.lab10, self.lab11, self.lab12, self.lab13, self.lab14, self.lab15, self.lab16 = Label(), Label(), Label(), Label(), Label(), Label(), Label()
		self.lab20, self.lab21, self.lab22, self.lab23, self.lab24, self.lab25, self.lab26 = Label(), Label(), Label(), Label(), Label(), Label(), Label()
		self.lab30, self.lab31, self.lab32, self.lab33, self.lab34, self.lab35, self.lab36 = Label(), Label(), Label(), Label(), Label(), Label(), Label()
		self.lab40, self.lab41, self.lab42, self.lab43, self.lab44, self.lab45, self.lab46 = Label(), Label(), Label(), Label(), Label(), Label(), Label()
		self.lab50, self.lab51, self.lab52, self.lab53, self.lab54, self.lab55, self.lab56 = Label(), Label(), Label(), Label(), Label(), Label(), Label()
		self.labs = [[self.lab00, self.lab01, self.lab02, self.lab03, self.lab04, self.lab05, self.lab06],
		        [self.lab10, self.lab11, self.lab12, self.lab13, self.lab14, self.lab15, self.lab16],
		        [self.lab20, self.lab21, self.lab22, self.lab23, self.lab24, self.lab25, self.lab26],
		        [self.lab30, self.lab31, self.lab32, self.lab33, self.lab34, self.lab35, self.lab36],
		        [self.lab40, self.lab41, self.lab42, self.lab43, self.lab44, self.lab45, self.lab46],
		        [self.lab50, self.lab51, self.lab52, self.lab53, self.lab54, self.lab55, self.lab56], ]
		for i in range(6):
			for j in range(7):
				self.labs[i][j].setFixedSize(88, 88)
				self.labs[i][j].clicked.connect(lambda : displayDate(self))
				self.gridWNL.addWidget(self.labs[i][j], i + 2, j)
		self.cblFindFestival = QComboBox()
		self.cblFindFestival.addItem('查找农历节日')
		for festival in lcfestivals:
			self.cblFindFestival.addItem(festival[-1])
		self.cblFindFestival.activated.connect(self.thisJumpFestival)
		self.cblFindFestival.setStyleSheet("QComboBox { leftPadding: 1px }")
		self.cblFindFestival.setMaximumWidth(150)
		self.cblFindFestival.setMaximumHeight(150)
		self.cblFindFestival.setStyleSheet("QComboBox{background:#F7D674}")
		self.hlayGL = QHBoxLayout()
		self.hlayGL.addWidget(self.cblFindFestival)
		self.labInfo = QLabel()
		self.labInfo.setStyleSheet("QLabel{ font:14px;}"
								   "QLabel{border-image: url(image/biankuang.jpg)}"#右侧日期信息背景
								   "QLabel{border-radius:9px}"  # 圆角
								   )
		self.labInfo.setAlignment(Qt.AlignHCenter)
		self.labInfo.setContentsMargins(0, 100, 0, 0)
		self.labInfo.setWordWrap(True)
		self.labInfo.setFixedWidth(300)
		#self.labInfo.move(0, 300)
		self.gridWNL.addLayout(self.hlayGL, 0, 7, 1, 1)
		self.gridWNL.addWidget(self.labInfo, 1, 7, 7, 1)

	def thisJumpMonth(self):
		if self.sender() == self.btnLastMonth:
			lastMonth(self)
		elif self.sender() == self.btnNextMonth:
			nextMonth(self)
		elif self.sender() == self.btnLastYear:
			lastYear(self)
		elif self.sender() == self.btnNextYear:
			nextYear(self)
		displayDate(self)

	def thisJumpFestival(self):
		if self.cblFindFestival.currentText() != '查找农历节日':
			pass
			displayDate(self)