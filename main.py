from PyQt5 import QtWidgets, uic, QtCore, QtOpenGL, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QThread, pyqtSignal
from PyQt5.QtGui import *
from boid import *
import sys, time
from random import randint

class Simu(QThread) :
	new_x=pyqtSignal(int,int)

	def run(self) :
		while True :
			self.update_pos()

	def update_pos(self) :
		x=randint(0, 1130-20)
		y=randint(0, 760-20)
		self.new_x.emit(x,y)
		time.sleep(.5)


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
        self.populate()
        self.simul=Simu()


    def populate(self) :
    	font = QtGui.QFont('White Rabbit')
    	font.setPointSize(120)
    	bobo=QPixmap('bobo.jpg')
    	self.l = QGraphicsPixmapItem(bobo)
    	self.l.setPos(10,200)
    	
    	
    	

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
    	self.simul.new_x.connect(self.update_pos)
    	if self.start_btn.text() == 'Start' :
    		self.start_btn.setText("Stop")
    		self.scene.addItem(self.l)
    		self.simul.start()


    	else :
    		self.start_btn.setText("Start")
    		self.simul.terminate()
    		self.scene.clear()

    def update_pos(self,x,y) :
    	self.l.setPos(x, y)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

