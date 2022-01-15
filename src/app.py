from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPixmap
import sys
from classes import Livre, Auteur, Bibliotheque
from ui import Ui_MainWindow
import utils.requetesOpenLibrary as rol


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.bib = Bibliotheque.Bibliotheque()
        self.bib.initBibliotheque()

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
        self.updateBib()
        self.ui.stackedWidget.setCurrentWidget(self.ui.bibliothequeWidget)

    def search(self):
        rol.globalSearch(self.ui.searchLineEdit.text(), self.ui)

    def updateBib(self):
        liste_livres = self.bib.getListeLivre()
        row = 0
        col = 0
        for livre in liste_livres:
            widget = QtWidgets.QWidget(self.ui.scrollAreaBibliothequeWidgetContent)
            widget.setObjectName(f"widget{row}{col}")
            verticalLayout = QtWidgets.QVBoxLayout(widget)
            verticalLayout.setObjectName(f"verticalLayoutBib_{row}{col}")
            label = QLabel(widget)
            pixmapImgNotFound = QPixmap('../assets/img/image_not_found.png')
            label.setPixmap(pixmapImgNotFound)
            verticalLayout.addWidget(label)

            label_livre = QtWidgets.QLabel(widget)
            label_livre.setObjectName(f"{livre.getTitre()}")
            label_auteur = QtWidgets.QLabel(widget)
            label_auteur.setObjectName(f"auteur{row}{col}")
            label_livre.setText(f"{livre.getTitre()}")
            if livre.getHasAuthor() == True :
                label_auteur.setText(f"Auteur : {livre.getAuthor()}")
            verticalLayout.addWidget(label_livre)
            verticalLayout.addWidget(label_auteur)
            if col < 3: # je vais vérifer ou nous somme dans la grille
                self.ui.gridLayout.addWidget(widget, row, col)
                col += 1
            elif col == 3: # si la colone  c'est 4 on ajoute et puis on change de ligne
                self.ui.gridLayout.addWidget(widget, row, col)
                col = 0
                row += 1

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
