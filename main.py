from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QThread, pyqtSignal
from PyQt5.QtGui import *
from boid import *
import sys, time
from random import randint
import numpy as np

class Simu(QThread) :
	
	new_x=pyqtSignal(np.ndarray,np.ndarray)

	def __init__(self, NoBoids, Speed, Distance, Cohesion):
		QThread.__init__(self)
		self.speed = Speed
		self.noBoids = NoBoids
		self.distance = Distance
		self.cohes = Cohesion
		

	def run(self) :
		angle = np.asarray([randint(0, 360)*pi/180 for _ in range(self.noBoids)])
		x = np.asarray([randint(0,1130) for _ in range(self.noBoids)])
		y = np.asarray([randint(0,760) for _ in range(self.noBoids)])
		while True :
			#for ji in range(self.noBoids) :
			#	x[ji],y[ji], angle[ji]=UpdateBoidPos(x[ji], y[ji], angle[ji], self.speed, self.distance, self.cohes)
			x, y, angle = UpdateBoidPos(x, y, angle, self.speed, self.distance, self.cohes)
			self.new_x.emit(x,y)
			time.sleep(.01)

	def update_pos(self, x, y, angle, speed) :
		x+= speed*sqrt(2) * cos(angle)
		y+= speed*sqrt(2) * sin(angle)
		if x >= 1130 :
			angle = (pi-angle)
		if x <= 0 :
			angle = pi-angle
		if y >= 760 :
			angle = (-angle)
		if y <= 0 :
			angle = -angle
		return x,y, angle
	def UpdateSpeed(self,val) :
		self.testspeed = val
		self.FlagChangedSlider = True


class Ui(QtWidgets.QMainWindow): #Classe de la fenetre d'application #
	def __init__(self):
		super(Ui, self).__init__() # Call the inherited classes __init__ method
		uic.loadUi('uiii.ui', self) # Load the .ui file
		self.setWindowTitle("ye booooids")

		self.Btn_Toggle.clicked.connect(self.toggle_menu)
		self.start_btn.clicked.connect(self.start_stop)
		self.qty_slider.valueChanged.connect(self.update_noboids)
		self.speed_slider.valueChanged.connect(self.update_speed)
		self.dist_slider.valueChanged.connect(self.update_distance)
		self.show()
		self.scene = QGraphicsScene(self)
		self.graph.setScene(self.scene)
		self.scene.setSceneRect(0,0,1130,760)
		self.cohesion = 0.5
		self.noboids = self.qty_slider.value()
		self.simul=Simu(self.qty_slider.value(), self.speed_slider.value(), self.dist_slider.value(), self.cohesion)
		self.simul.new_x.connect(self.update_pos)


	def populate(self) :
		self.circles = []
		self.simul = Simu(self.qty_slider.value(), self.speed_slider.value(), self.dist_slider.value(), self.cohesion)
		self.simul.new_x.connect(self.update_pos)
		for _ in range (self.noboids) :
			self.circles.append(QGraphicsPixmapItem(QPixmap('boid.png')))
		for ii in enumerate(self.circles) :
			self.circles[ii[0]].setPos(randint(0,1130), randint(0,760))


		

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
			self.animation.setDuration(200)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.start()

	def start_stop(self) :
		self.simul.new_x.connect(self.update_pos)
		if self.start_btn.text() == 'Start' :
			self.start_btn.setText("Stop")
			self.populate()
			for i in range (self.noboids) :
				self.scene.addItem(self.circles[i])
			self.simul.start()
			
		else :
			self.start_btn.setText("Start")
			self.scene.clear()
			self.simul.terminate()
			self.simul.wait()
			print('Proccess stoped')

	def update_pos(self,x,y) :
		try :
			for i in range (self.noboids) :
				self.circles[i].setPos(x[i],y[i])
		except :
			self.simul.terminate()
			self.simul.wait()

	def update_noboids(self) :
		if self.start_btn.text()=='Stop' :
			self.start_stop()
			self.noboids = self.qty_slider.value()
			self.start_stop()
		else : 
			self.noboids = self.qty_slider.value()
	
	def update_speed(self) :
		if self.start_btn.text()=='Stop' :
			self.start_stop()
			self.start_stop()
		else :
			pass
	
	def update_distance(self) :
		if self.start_btn.text()=='Stop' :
			self.start_stop()
			self.start_stop()
		else :
			pass
	


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
sys.exit()
