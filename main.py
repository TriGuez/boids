from PyQt5 import QtWidgets, uic
import sys



class Ui(QtWidgets.QMainWindow): #Classe de la fenetre d'application #
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('uiii.ui', self) # Load the .ui file
        self.showMaximized()
        self.setWindowTitle("Application")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
