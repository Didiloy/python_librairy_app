from functools import partial

import requests
import urllib.request
import urllib
import json
import os
from PyQt5 import QtWidgets, uic

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.uic.properties import QtCore

sys.path.append("..") # Adds higher directory to python modules path.

from src.classes import Bibliotheque
from src.classes import Livre
from src.ui import Ui_MainWindow
from src.app import  MainWindow


class RequetesOpenLibrary:
    def __init__(self, biblio, uiArg):
        self.dico_livres_boutons = {}
        self.bib = biblio
        self.ui = uiArg

    def globalSearch(self, search):
        # remettre le label a 0
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
                    if 'publishedDate' in volumeInfo and volumeInfo['publishedDate'] != None:
                        liste_livre[i].setDateDeParution(volumeInfo['publishedDate'])
                    i += 1
                hasCover = False

            #####afficher les résultats
            row = 0
            col = 0
            self.dico_livres_boutons.clear()
            for livre in liste_livre:
                self.ui.labelRechercheEnCours.setText("Recherche en cours...")
                QApplication.processEvents()
                widget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)  # Je crée un widget qui contiendra la cover du livre, le titre et l'auteur
                widget.setObjectName(f"widgetScrollAreaAnswer{row}{col}")
                verticalLayout = QtWidgets.QVBoxLayout(widget)  # Je defini le layout pour contenir les informations du livre
                verticalLayout.setObjectName(f"verticalLayoutSearch_{row}{col}")
                label = QLabel(widget)
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
                    label.setPixmap(pixmap)
                else:
                    label.setPixmap(pixmapImgNotFound)
                verticalLayout.addWidget(label)

                label_livre = QtWidgets.QLabel(widget)  # Je crée le label du livre
                label_livre.setObjectName(f"{livre.getTitre()}")
                label_livre.setGeometry(100, 150, 50, 50)
                label_livre.setWordWrap(True)

                label_auteur = QtWidgets.QLabel(widget)  # Je crée le label de l'auteur
                label_auteur.setObjectName(f"auteur{row}{col}")
                label_auteur.setGeometry(100, 150, 50, 50)
                label_auteur.setWordWrap(True)

                addButton = QtWidgets.QPushButton(widget)
                addButton.setObjectName(f"addButton{row}{col}")
                # print(addButton.objectName())
                addButton.setText("ajouter à la bibliothèque")
                # addButton.setGeometry(50, 30, 0, 0)
                addButton.setFixedWidth(170)
                self.dico_livres_boutons[livre] = addButton

                label_livre.setText(f"{livre.getTitre()}")
                if livre.getHasAuthor() == True:
                    label_auteur.setText(f"Auteur : {livre.getAuthor()}")  # Si le livre à un auteur on ajoute son nom
                verticalLayout.addWidget(label_livre)
                verticalLayout.addWidget(label_auteur)
                verticalLayout.addWidget(addButton)

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
        self.bib.addBook(livre)
        self.bib.writeToJSONFile()

    def downloadCovers(self, id, name):
        url = id
        pathToImg = os.path.join("..", "assets", "img", name)
        urllib.request.urlretrieve(url, pathToImg)  # télécharger l'image