from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
import sys
from classes import Livre, Auteur, Bibliotheque
from ui import Ui_MainWindow
import utils.requetesOpenLibrary as rol


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.homeWidget)  # je met le panel de base au milieu
        self.ui.leftPanelButtonHome.clicked.connect(self.showHome)  # j'ajoute une action au bouton pour afficher le bon panel
        self.ui.leftPanelButtonSearch.clicked.connect(self.showSearch)  # j'ajoute une action au bouton pour afficher le bon panel
        self.ui.leftPanelButtonBibliotheque.clicked.connect(self.showBiblio)  # j'ajoute une action au bouton pour afficher le bon panel

        self.ui.searchButton.clicked.connect(self.search)  # j'ajoute la fonction pour rechercher au bouton

    def getUi(self):
        return self.ui

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homeWidget)

    def showSearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.searchWidget)

    def showBiblio(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bibliothequeWidget)

    def search(self):
        rol.globalSearch(self.ui.searchLineEdit.text(), self.ui)

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qss = "../assets/stylesheet/qdarkgraystyle.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
