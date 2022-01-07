import requests
import urllib.request
import json
import os

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from src.classes import Auteur
from src.classes import Livre
from src.ui import Ui_MainWindow
import app


def globalSearch(search, uiArg):
    ui = uiArg
    # remettre le label a 0
    ui.answerLabel.setText("")
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
        if i >= 5:
            break
        if 'cover_edition_key' in books and books['cover_edition_key'] != None:
            hasCover = True
            # print(f"cover id : {books['cover_edition_key']}")
            # downloadCovers(books['cover_edition_key'])

        if 'author_name' not in books or books['author_name'] == None or books['author_name'] == []:
            # print('Livre: ' + str(books['title']) + ' et pas d\'auteur')
            liste_livre.append(Livre.Livre(str(books['title'])))
            # print(liste_livre[i].toString())
            texte = ui.answerLabel.text() + str(liste_livre[i].toString())
            ui.answerLabel.setText(texte)
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        else:
            # print('Livre: ' + str(books['title']) + ' par l\'auteur ' + str(books['author_name'][-1]) )
            liste_livre.append(Livre.Livre(str(books['title'])))
            liste_livre[i].setAuthor(str(books['author_name'][-1]))
            # print(liste_livre[i].toString())
            texte = ui.answerLabel.text() + str(liste_livre[i].toString())
            ui.answerLabel.setText(texte)
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        hasCover = False
