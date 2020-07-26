# coding : utf-8 
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QThread, pyqtSignal
from PyQt5.QtGui import *
from boid import *
import sys, time
from random import randint
from math import pi

class Simu(QThread) :
	new_positions=pyqtSignal(int,int,int)
	

	def run(self,nb_boids) : 
		
		self.flock = [boid(randint(0,1130),randint(0,760),1,(120 * pi /180)) for _ in range (nb_boids)] # création de tout les boids
		
		'''while True :
			self.movement()
			time.sleep(.1)'''
		for _ in range (10) :
			i=0
			for k in self.flock :
				k.boidBehave()
				self.new_positions.emit(k.get_x(),k.get_y(),i)
				i=i+1
		time.sleep(.1)






class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__() 
		uic.loadUi('uiii.ui', self) 
		self.setWindowTitle("ye booooids")

		self.Btn_Toggle.clicked.connect(self.toggle_menu)
		self.start_btn.clicked.connect(self.start_stop)
		self.show()
		self.scene = QGraphicsScene(self)
		self.graph.setScene(self.scene)
		self.scene.setSceneRect(0,0,1130,760)
		self.noboids = 100
		self.simul=Simu()
		self.isPopulate = False


	def populate(self) : # si le flag is_populate est False, on remplit la scnène avec les petits cercles
		self.boids = [QGraphicsPixmapItem(QPixmap("boid.png")) for _ in range (self.noboids)] # creéation des petits cercles correspondants à chaque boid #
		for k in self.boids :
			self.scene.addItem(k)
		self.isPopulate = True
		
		

	def toggle_menu(self) : #pour el menu dépliant
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

	def start_stop(self) : # on lance le thread de calcul des positions, ou alors on l'arrête suvant l'affichage du bouton Start/stop
		self.simul.new_positions.connect(self.update_pos) # on "connecte" le signal de la liste envoyé par le thread a chaque déplacement des boids à la foncton update_pos
		if self.start_btn.text() == 'Start' :
			self.start_btn.setText("Stop")
			self.simul.run(self.noboids)


		else :
			self.start_btn.setText("Start")
			self.simul.terminate()
			self.scene.clear()
			self.isPopulate = False

	def update_pos(self,x,y,i) :
		if not self.isPopulate :
			self.populate() #si la scene est vide, on la rempli
		else :
			self.boids[i].setPos(x,y)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
sys.exit()
