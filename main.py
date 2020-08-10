from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QThread, pyqtSignal
from PyQt5.QtGui import *
from boid import *
import sys, time
from random import randint
from math import pi

class Simu(QThread) :
	new_x=pyqtSignal(int,int)
	

	def run(self) :
		self.flock = boid(randint(0,1130),randint(0,760),1,120)
		while True :
			x,y=self.update_pos()
			self.new_x.emit(x,y)
			time.sleep(.1)

	def update_pos(self) :
		self.flock.boidBehave()
		x=self.flock.get_x()
		y=self.flock.get_y()
		return x,y
		


class Ui(QtWidgets.QMainWindow): #Classe de la fenetre d'application #
	def __init__(self):
		super(Ui, self).__init__() # Call the inherited classes __init__ method
		uic.loadUi('uiii.ui', self) # Load the .ui file
		self.setWindowTitle("ye booooids")

		self.Btn_Toggle.clicked.connect(self.toggle_menu)
		self.start_btn.clicked.connect(self.start_stop)
		self.show()
		self.scene = QGraphicsScene(self)
		self.graph.setScene(self.scene)
		self.scene.setSceneRect(0,0,1130,760)
		self.noboids = 2
		self.simul=Simu()


	def populate(self) :
		self.circles = []
		self.threads = []
		for _ in range (self.noboids) :
			self.circles.append(QGraphicsPixmapItem(QPixmap('boid.png')))
			self.threads.append(Simu())

		

	def toggle_menu(self) : 
		maxWidth = 250
		enable = True
		if enable : 
			width = self.frame_left_menu.width()
			maxExtend = maxWidth
			standard = 70

			if width == 70 :
				widthExtended = maxExtend
			else :
				widthExtended = standard
			self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
			self.animation.setDuration(400)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.start()

	def start_stop(self) :
		#self.simul.new_x.connect(self.update_pos)
		if self.start_btn.text() == 'Start' :
			self.start_btn.setText("Stop")
			self.populate()
			for i in range (self.noboids) :
				self.scene.addItem(self.circles[i])
				self.threads[i].new_x.connect(self.update_pos)
				self.threads[i].start()


		else :
			self.start_btn.setText("Start")
			self.scene.clear()
			for i in range (self.noboids) :
				self.threads[i].terminate()

	def update_pos(self,x,y) :
		for i in range (self.noboids) :
			self.circles[i].setPos(x,y)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
sys.exit()
