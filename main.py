from PyQt5 import QtWidgets, uic, QtCore, QtOpenGL
from PyQt5.QtCore import QPropertyAnimation
import sys
from OpenGL import GL
from boid import *
#Jessaie un truc
class Ui(QtWidgets.QMainWindow): #Classe de la fenetre d'application #
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('uiii.ui', self) # Load the .ui file
        self.setWindowTitle("ye booooids")

        self.Btn_Toggle.clicked.connect(self.toggle_menu)
        self.start_btn.clicked.connect(self.start_stop)
        self.show()

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
    	if self.start_btn.text() == 'Start' :
    		self.start_btn.setText("Stop")
    		self.gl.glBegin(GL_QUADS)
    		self.gl.glVertex2f(100,100)
    	else :
    		self.start_btn.setText("Start")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

