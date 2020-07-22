from PyQt5 import QtWidgets, uic, QtCore, QtOpenGL
from PyQt5.QtCore import QPropertyAnimation
import sys
from OpenGL import GL
from boid import *

class Ui(QtWidgets.QMainWindow): #Classe de la fenetre d'application #
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('uiii.ui', self) # Load the .ui file
        self.setWindowTitle("ye booooids")

        self.Btn_Toggle.clicked.connect(self.toggle_menu)
        self.show()

    def toggle_menu(self) : 
        maxWidth = 250
        enable = True
        if enable : 
        	width = self.frame_left_menu.width()
        	maxExtend = maxWidth
        	standard = 0

        	if width == 0 :
        		widthExtended = maxExtend
        	else :
        		widthExtended = standard
        	self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
        	self.animation.setDuration(400)
        	self.animation.setStartValue(width)
        	self.animation.setEndValue(widthExtended)
        	self.animation.start()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

