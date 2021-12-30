from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
import sys

class WelcomeWindow(QMainWindow):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle("Library App")
        self.initUI()

    def initUI(self):
        self.welcome = QtWidgets.QLabel(self)
        self.welcome.setText("Bienvenue dans la Library App")
        self.welcome.setFont(QFont('Times New Roman', 50))
        self.welcome.adjustSize()
        self.welcome.move(20, 50)
        self.update()

        self.inscription_button = QtWidgets.QPushButton(self)
        self.inscription_button.setText("S'inscrire")
        self.inscription_button.move(300, 150)
        self.inscription_button.clicked.connect(self.inscription)

        self.connect_button = QtWidgets.QPushButton(self)
        self.connect_button.setText("Se connecter")
        self.connect_button.move(800, 150)
        self.connect_button.clicked.connect(self.connexion)

    def inscription(self):
        print("aller sur la page d'inscription")

    def connexion(self):
        print("aller sur la page de connexion")

def window():
    app = QApplication(sys.argv)
    win = WelcomeWindow()


    win.show()
    sys.exit(app.exec_())

window()
