from functools import partial

import requests
import urllib.request
import urllib
import json
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtGui

import sys

# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.uic.properties import QtCore

sys.path.append("..") # Adds higher directory to python modules path.

from src.classes import Bibliotheque
from src.classes import Livre
from src.ui import Ui_MainWindow
from src.app import  MainWindow


class RequetesOpenLibrary:
    def __init__(self, biblio, uiArg):
        self.dico_livres_boutons = {}
        self.dico_livres_boutons_cover = {}
        self.bib = biblio
        self.ui = uiArg

    def globalSearch(self, search):
        # remettre le label_cover_livre a 0
        search = self.ui.searchLineEdit.text()
        self.ui.searchLineEdit.setText("")
        # Making a get request
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search}&printType=books&maxResults=30')
        answerJson = os.path.join("..", "answer.json")
        fileToWrite = open(answerJson, 'w+')  # Ecrire la reponse au format json dans un fichier json
        fileToWrite.write(response.text)
        fileToWrite.close()
        data = json.loads(response.text)  # Transformer le texte en objet json
        i = 0
        liste_livre = []
        hasCover = False
        if 'items' in data and data['items'] != None :
            for books in data['items']:
                volumeInfo = books['volumeInfo']
                if 'imageLinks' in volumeInfo and volumeInfo['imageLinks'] != None :
                    coversLink = volumeInfo['imageLinks']
                    hasCover = True

                if 'authors' not in volumeInfo or volumeInfo['authors'] == None or volumeInfo['authors'] == []:
                    liste_livre.append(Livre.Livre(str(volumeInfo['title'])))
                    if hasCover:
                        liste_livre[i].setCoverID(str(books['id'])) # je met l'id du livre comme id de cover
                        liste_livre[i].setCoverLink(coversLink['thumbnail'])
                    i += 1
                else:
                    liste_livre.append(Livre.Livre(str(volumeInfo['title'])))
                    liste_livre[i].setAuthor(str(volumeInfo['authors'][0]))
                    liste_livre[i].setHasAuthor(True)
                    if hasCover:
                        liste_livre[i].setCoverID(str(books['id']))
                        liste_livre[i].setCoverLink(coversLink['thumbnail'])
                    if 'publishedDate' in volumeInfo and volumeInfo['publishedDate'] != None: # Si il y a une date de publication
                        liste_livre[i].setDateDeParution(volumeInfo['publishedDate'])
                    if 'description' in volumeInfo and volumeInfo['description'] != None : # Si il y a une description
                        liste_livre[i].setResume(volumeInfo['description'])
                    i += 1
                hasCover = False

            #####afficher les résultats
            row = 0
            col = 0
            self.dico_livres_boutons.clear()
            self.dico_livres_boutons_cover.clear()
            for livre in liste_livre:
                self.ui.labelRechercheEnCours.setText("Recherche en cours...")
                QApplication.processEvents()
                widget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)  # Je crée un widget qui contiendra la cover du livre, le titre et l'auteur
                widget.setObjectName(f"widgetScrollAreaAnswer{row}{col}")
                verticalLayout = QtWidgets.QVBoxLayout(widget)  # Je defini le layout pour contenir les informations du livre
                verticalLayout.setObjectName(f"verticalLayoutSearch_{row}{col}")
                # label_cover_livre = QLabel(widget)
                button_cover_livre = QtWidgets.QPushButton(widget)
                button_cover_livre.setStyleSheet("border-style: none")
                imgNotFound = os.path.join("..","assets","img","image_not_found.png")
                # pixmapImgNotFound = QPixmap('../assets/img/image_not_found.png')
                pixmapImgNotFound = QPixmap(imgNotFound)
                pixmapImgNotFound = pixmapImgNotFound.scaled(100, 140)

                if livre.coverId != None:
                    url = livre.getCoverLink()
                    data = urllib.request.urlopen(url).read()
                    pixmap = QPixmap()
                    pixmap.loadFromData(data)
                    pixmap = pixmap.scaled(100, 140)
                    # label_cover_livre.setPixmap(pixmap)
                    button_cover_livre.setIcon(QtGui.QIcon(pixmap))
                    button_cover_livre.setIconSize(QSize(100, 140))
                else:
                    # label_cover_livre.setPixmap(pixmapImgNotFound)
                    button_cover_livre.setIcon(QtGui.QIcon(pixmapImgNotFound))
                    button_cover_livre.setIconSize(QSize(100, 140))
                # verticalLayout.addWidget(label_cover_livre)
                verticalLayout.addWidget(button_cover_livre)

                label_livre = QtWidgets.QLabel(widget)  # Je crée le label_cover_livre du livre
                label_livre.setObjectName(f"{livre.getTitre()}")
                label_livre.setGeometry(100, 150, 50, 50)
                label_livre.setAlignment(Qt.AlignCenter)
                label_livre.setWordWrap(True)

                label_auteur = QtWidgets.QLabel(widget)  # Je crée le label_cover_livre de l'auteur
                label_auteur.setObjectName(f"auteur{row}{col}")
                label_auteur.setGeometry(100, 150, 50, 50)
                label_auteur.setAlignment(Qt.AlignCenter)
                label_auteur.setWordWrap(True)

                addButton = QtWidgets.QPushButton(widget)
                addButton.setObjectName(f"addButton{row}{col}")
                # print(addButton.objectName())
                addButton.setText("ajouter à la bibliothèque")
                # addButton.setGeometry(50, 30, 0, 0)
                addButton.setFixedWidth(170)
                # addButton.setAlignment(Qt.AlignCenter)
                self.dico_livres_boutons[livre] = addButton
                self.dico_livres_boutons_cover[livre] = button_cover_livre

                label_livre.setText(f"{livre.getTitre()}")
                if livre.getHasAuthor() == True:
                    label_auteur.setText(f"Auteur : {livre.getAuthor()}")  # Si le livre à un auteur on ajoute son nom
                verticalLayout.addWidget(label_livre)
                verticalLayout.addWidget(label_auteur)
                verticalLayout.addWidget(addButton, alignment=Qt.AlignCenter)

                if col < 2:  # je vais vérifer ou nous somme dans la grille
                    self.ui.gridLayout_2.addWidget(widget, row, col)
                    col += 1
                elif col == 2:  # si la colone  c'est 4 on ajoute et puis on change de ligne
                    self.ui.gridLayout_2.addWidget(widget, row, col)
                    col = 0
                    row += 1
                self.ui.labelRechercheEnCours.setText("Recherche en cours..")
                QApplication.processEvents()
            self.addBoutonListener()
            self.addBoutonCoverLivreListener()
            # print(self.dico_livres_boutons)
            self.ui.labelRechercheEnCours.setText(f"{i} livres trouvés")
        else: 
            self.ui.labelRechercheEnCours.setText("Pas de résultat pour votre recherche")


    def addBoutonListener(self):
        for livre in self.dico_livres_boutons:
            # self.dico_livres_boutons.get(livre).clicked.connect(lambda: self.boutonAjouterBib(livre))
            # self.dico_livres_boutons.get(livre).clicked.connect(lambda state, x=livre: self.boutonAjouterBib(x))
            # print(f"{livre} : {livre.getTitre()} -> {self.dico_livres_boutons.get(livre)} : {self.dico_livres_boutons.get(livre).objectName()}")
            self.dico_livres_boutons.get(livre).clicked.connect(partial(self.boutonAjouterBib, livre))



    def boutonAjouterBib(self, livre):
        if livre.coverId != None:
            self.downloadCovers(livre.getCoverLink(), livre.getCoverID())
        if livre.getResume() != None:
            print("le livre à un résumé")
        self.bib.addBook(livre)
        self.bib.writeToJSONFile()

    def downloadCovers(self, id, name):
        url = id
        pathToImg = os.path.join("..", "assets", "img", name)
        urllib.request.urlretrieve(url, pathToImg)  # télécharger l'image

    def addBoutonCoverLivreListener(self): # ajouter les listener pour chaque boutons avec la cover du livre
        for livre in self.dico_livres_boutons_cover:
            self.dico_livres_boutons_cover.get(livre).clicked.connect(partial(self.button_cover_livre_handler, livre))

    def button_cover_livre_handler(self, livre): # montrer le panel de détail du livre
        if livre.coverId != None: # Si le livre à une cover
            url = livre.getCoverLink()
            data = urllib.request.urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(200, 260)
            self.ui.bookDetailCoverLabel.setPixmap(pixmap)
        else: # Si le livre n'en a pas
            imgNotFound = os.path.join("..", "assets", "img", "image_not_found.png")
            pixmapImgNotFound = QPixmap(imgNotFound)
            pixmapImgNotFound = pixmapImgNotFound.scaled(200, 260)
            self.ui.bookDetailCoverLabel.setPixmap(pixmapImgNotFound)

        self.ui.bookDetailAuthorLabel.setText(livre.getAuthor()) # Mettre le nom de l'auteur
        self.ui.bookDetailTitleLabel.setText(livre.getTitre()) # Mettre le titre
        if livre.getResume() == None: # Si il n'y a pas de résumé
            self.ui.bookDetailDescriptionLabel.setText("Pas de résumé disponible.")
        else :
            self.ui.bookDetailDescriptionLabel.setText(livre.getResume()) # Mettre le résumé
        self.ui.stackedWidget.setCurrentWidget(self.ui.bookDetailWidget) # Montrer le panel