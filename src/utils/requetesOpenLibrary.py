import requests
import urllib.request
import urllib
import json
import os
from PyQt5 import QtWidgets, uic

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

sys.path.append("..") # Adds higher directory to python modules path.

from src.classes import Auteur
from src.classes import Livre
from src.ui import Ui_MainWindow
import app


def globalSearch(search, uiArg):
    ui = uiArg
    # remettre le label a 0
    search = ui.searchLineEdit.text()
    ui.searchLineEdit.setText("")

    # Making a get request
    response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything')

    fileToWrite = open('../answer.json', 'w+')  # Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text)  # Transformer le texte en objet json
    i = 0
    liste_livre = []
    hasCover = False
    for books in data['docs']:
        if 'cover_edition_key' in books and books['cover_edition_key'] != None:
            hasCover = True

        if 'author_name' not in books or books['author_name'] == None or books['author_name'] == []:
            liste_livre.append(Livre.Livre(str(books['title'])))
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        else:
            liste_livre.append(Livre.Livre(str(books['title'])))
            liste_livre[i].setAuthor(str(books['author_name'][-1]))
            liste_livre[i].setHasAuthor(True)
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        hasCover = False

    #####afficher les résultats
    row = 0
    col = 0
    for livre in liste_livre:
        widget = QtWidgets.QWidget(ui.scrollAreaWidgetContents)  # Je crée un widget qui contiendra la cover du livre, le titre et l'auteur
        widget.setObjectName(f"widgetScrollAreaAnswer{row}{col}")
        verticalLayout = QtWidgets.QVBoxLayout(widget)  # Je defini le layout pour contenir les informations du livre
        verticalLayout.setObjectName(f"verticalLayoutSearch_{row}{col}")
        label = QLabel(widget)
        pixmapImgNotFound = QPixmap('../assets/img/image_not_found.png')
        pixmapImgNotFound = pixmapImgNotFound.scaled(100, 140)

        if livre.coverId != None:
            url = f'https://covers.openlibrary.org/b/olid/{livre.coverId}-M.jpg'
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
        addButton.setText("ajouter à la bibliothèque")
        # addButton.setGeometry(50, 30, 0, 0)
        addButton.setFixedWidth(170)

        label_livre.setText(f"{livre.getTitre()}")
        if livre.getHasAuthor() == True:
            label_auteur.setText(f"Auteur : {livre.getAuthor()}")  # Si le livre à un auteur on ajoute son nom
        verticalLayout.addWidget(label_livre)
        verticalLayout.addWidget(label_auteur)
        verticalLayout.addWidget(addButton)

        if col < 2:  # je vais vérifer ou nous somme dans la grille
            ui.gridLayout_2.addWidget(widget, row, col)
            col += 1
        elif col == 2:  # si la colone  c'est 4 on ajoute et puis on change de ligne
            ui.gridLayout_2.addWidget(widget, row, col)
            col = 0
            row += 1
