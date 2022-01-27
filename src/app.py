import json
import os
import urllib
from functools import partial
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from wand.image import Image
import requests
from PyQt5 import QtWidgets, uic, QtGui
import asyncio
import time
import sys
from classes import Livre, Auteur, Bibliotheque
from ui import Ui_MainWindow
import utils.requetesOpenLibrary as rol


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.main_win.setWindowTitle("Bibliothèque")
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.bib = Bibliotheque.Bibliotheque().getInstance()
        self.rol = rol.RequetesOpenLibrary(self.bib, self.ui)
        self.dico_boutons_supprimer_livre = {}
        self.dico_livres_boutons_cover = {}

        self.ui.stackedWidget.setCurrentWidget(self.ui.homeWidget)  # je met le panel de base au milieu
        self.ui.leftPanelButtonHome.clicked.connect(self.showHome)  # j'ajoute une action au bouton pour afficher le bon panel
        self.ui.leftPanelButtonSearch.clicked.connect(self.showSearch)  # j'ajoute une action au bouton pour afficher le bon panel
        self.ui.bookDetaillRetourButton.clicked.connect(self.showSearch) # afficher le panel de recherche quand le bouton est cliqué
        self.ui.leftPanelButtonBibliotheque.clicked.connect(self.showBiblio)  # j'ajoute une action au bouton pour afficher le bon panel
        self.ui.buttonBlague.clicked.connect(self.getRandomComic)

        self.ui.searchButton.clicked.connect(self.search)  # j'ajoute la fonction pour rechercher au bouton

    def getUi(self):
        return self.ui

    def showHome(self): # Recommendations
        self.getRandomComic()
        QApplication.processEvents()
        self.ui.stackedWidget.setCurrentWidget(self.ui.homeWidget)

    def showSearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.searchWidget)

    def showBiblio(self):
        self.updateBib()
        self.ui.stackedWidget.setCurrentWidget(self.ui.bibliothequeWidget)

    def search(self):
        self.ui.labelRechercheEnCours.setText("Recherche en cours..")
        QApplication.processEvents() # ecouter les autres event de la fenetre pour les traiter. Ici afficher le label recherche en cours pendant qu'on cherche les livres
        self.rol.globalSearch(self.ui.searchLineEdit.text())

    def getRandomComic(self):
        rand = random.randint(1, 2572)
        QApplication.processEvents()
        reponse = requests.get(f'https://xkcd.com/{rand}/info.0.json')
        QApplication.processEvents()
        data = json.loads(reponse.text)
        url = data['img']
        img = urllib.request.urlopen(url).read()
        f = urllib.request.urlopen(url)  # avoir les dimensions de l'image
        with Image(file=f) as imgf:
            width = imgf.width
            height = imgf.height
            # print(f"width : {width} | height : {height}")
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        pixmap = pixmap.scaled(width, height)
        QApplication.processEvents()
        self.ui.labelImageBlague.setPixmap(pixmap)


    def updateBib(self):
        # print(self.ui.scrollAreaBibliothequeWidgetContent.children())
        for widget in self.ui.scrollAreaBibliothequeWidgetContent.children(): # Supprimer tout les éléments graphique créés dans la bibliothèque
            if widget.objectName() != "gridLayout" and widget.objectName() != "widget": # ne pas supprimer ces deux là car ce sont ceux dans lesquels sont ajoutés les widgets des livres
                widget.deleteLater()
        self.dico_boutons_supprimer_livre.clear()
        self.dico_livres_boutons_cover.clear()
        self.bib.writeToJSONFile()
        liste_livres = self.bib.getListeLivre()
        row = 0
        col = 0
        for livre in liste_livres:
            widget = QtWidgets.QWidget(self.ui.scrollAreaBibliothequeWidgetContent) # Je crée un widget qui contiendra la cover du livre, le titre et l'auteur
            widget.setObjectName(f"widget{row}{col}")
            verticalLayout = QtWidgets.QVBoxLayout(widget) # Je defini le layout pour contenir les informations du livre
            verticalLayout.setObjectName(f"verticalLayoutBib_{row}{col}")
            # label = QLabel(widget)
            button_cover_livre = QtWidgets.QPushButton(widget)
            button_cover_livre.setStyleSheet("border-style: none")
            imgNotFound = os.path.join("..","assets","img","image_not_found.png")
            # pixmapImgNotFound = QPixmap('../assets/img/image_not_found.png')
            pixmapImgNotFound = QPixmap(imgNotFound)
            pixmapImgNotFound = pixmapImgNotFound.scaled(100, 140)

            if livre.coverId != None:
                pathToCover = os.path.join("..", "assets", "img", livre.coverId)
                if os.path.exists(pathToCover): # Si le fichier existe
                    pixmapLivre = QPixmap(pathToCover)
                    pixmapLivre = pixmapLivre.scaled(100, 140)
                    # label.setPixmap(pixmapLivre)
                    button_cover_livre.setIcon(QtGui.QIcon(pixmapLivre))
                    button_cover_livre.setIconSize(QSize(100, 140))
                else: # Si le fichier n'existe pas
                    # label.setPixmap(pixmapImgNotFound)
                    button_cover_livre.setIcon(QtGui.QIcon(pixmapImgNotFound))
                    button_cover_livre.setIconSize(QSize(100, 140))
            else:
                # label.setPixmap(pixmapImgNotFound)
                button_cover_livre.setIcon(QtGui.QIcon(pixmapImgNotFound))
                button_cover_livre.setIconSize(QSize(100, 140))
            # verticalLayout.addWidget(label)
            verticalLayout.addWidget(button_cover_livre)

            label_livre = QtWidgets.QLabel(widget) # Je crée le label du livre
            label_livre.setObjectName(f"{livre.getTitre()}")
            label_livre.setGeometry(100, 150, 50, 50)
            label_livre.setAlignment(Qt.AlignCenter)
            label_livre.setWordWrap(True)

            label_auteur = QtWidgets.QLabel(widget) # Je crée le label de l'auteur
            label_auteur.setObjectName(f"auteur{row}{col}")
            label_auteur.setGeometry(100, 150, 50, 50)
            label_auteur.setAlignment(Qt.AlignCenter)
            label_auteur.setWordWrap(True)

            RmButton = QtWidgets.QPushButton(widget)
            RmButton.setObjectName(f"RmButton{row}{col}")
            # print(addButton.objectName())
            RmButton.setText("supprimer")
            # addButton.setGeometry(50, 30, 0, 0)
            RmButton.setFixedWidth(170)
            self.dico_boutons_supprimer_livre[livre] = RmButton
            self.dico_livres_boutons_cover[livre] = button_cover_livre

            label_livre.setText(f"{livre.getTitre()}")
            if livre.getHasAuthor() == True :
                label_auteur.setText(f"Auteur : {livre.getAuthor()}") # Si le livre à un auteur on ajoute son nom
            verticalLayout.addWidget(label_livre)
            verticalLayout.addWidget(label_auteur)
            verticalLayout.addWidget(RmButton, alignment=Qt.AlignCenter)

            if col < 2: # je vais vérifer ou nous somme dans la grille
                self.ui.gridLayout.addWidget(widget, row, col)
                col += 1
            elif col == 2: # si la colone  c'est 4 on ajoute et puis on change de ligne
                self.ui.gridLayout.addWidget(widget, row, col)
                col = 0
                row += 1
            # print(widget.parentWidget().objectName()) # trouve le nom du parent auxquelles les widgets sont ajoutés
        self.addListenerBoutonSupprimerLivre()
        self.addBoutonCoverLivreListener()


    def addBoutonCoverLivreListener(self):
        for livre in self.dico_livres_boutons_cover:
            self.dico_livres_boutons_cover.get(livre).clicked.connect(partial(self.button_cover_livre_handler, livre))

    def button_cover_livre_handler(self, livre): # montrer le panel de détail du livre
        imgNotFound = os.path.join("..", "assets", "img", "image_not_found.png")
        pixmapImgNotFound = QPixmap(imgNotFound)
        pixmapImgNotFound = pixmapImgNotFound.scaled(200, 260)

        if livre.getCoverID() != None: # Si le livre à une cover
            pathToCover = os.path.join("..", "assets", "img", livre.getCoverID())
            if os.path.exists(pathToCover):  # Si le fichier existe
                pixmapLivre = QPixmap(pathToCover)
                pixmapLivre = pixmapLivre.scaled(200, 260)
                self.ui.bookDetailCoverLabel.setPixmap(pixmapLivre)
            else : # Si le fichier n'existe pas
                self.ui.bookDetailCoverLabel.setPixmap(pixmapImgNotFound)
        else: # Si le livre n'en a pas
            self.ui.bookDetailCoverLabel.setPixmap(pixmapImgNotFound)

        self.ui.bookDetailAuthorLabel.setText(livre.getAuthor()) # Mettre le nom de l'auteur
        self.ui.bookDetailTitleLabel.setText(livre.getTitre()) # Mettre le titre
        if livre.getResume() == None: # Si il n'y a pas de résumé
            self.ui.bookDetailDescriptionLabel.setText("Pas de résumé disponible.")
        else :
            self.ui.bookDetailDescriptionLabel.setText(livre.getResume()) # Mettre le résumé
        self.ui.stackedWidget.setCurrentWidget(self.ui.bookDetailWidget) # Montrer le panel

    def addListenerBoutonSupprimerLivre(self):
        for livre in self.dico_boutons_supprimer_livre:
            self.dico_boutons_supprimer_livre.get(livre).clicked.connect(partial(self.boutonSupprimerLivre, livre))

    def boutonSupprimerLivre(self, livre):
        self.bib.removeBook(livre)
        self.updateBib()
        

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pathToQss = os.path.join("..", "assets", "stylesheet", "qdarkgraystyle.qss")
    qss = pathToQss
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
