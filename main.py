from PyQt5 import QtWidgets, uic, QtCore, QtOpenGL
import sys
from OpenGL import GL
from boid import *

class Ui(QtWidgets.QMainWindow): #Classe de la fenetre d'application #
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('uiii.ui', self) # Load the .ui file
        self.setWindowTitle("ye booooids")
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

