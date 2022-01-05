from PyQt5 import QtWidgets, uic
import requests
import urllib.request
import json
import os
dir = os.getcwd() #avoir le dossier dans lequel on est pour faciliter les imports
classes = dir + "/classes/"
import sys
sys.path.append(classes)
print(sys.path)
from Auteur import Auteur
from Livre import Livre

def searchOpenLibrary():
    #remettre le label a 0
    searchUi.answerLabel.setText("")

    search = searchUi.lineEditSearch.text()
    searchUi.lineEditSearch.setText("")
    # Making a get request
    response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything')

    fileToWrite = open('answer.json', 'w+') #Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text) #Transformer le texte en objet json
    i = 0
    liste_livre = []
    hasCover = False
    for books in data['docs']:
        if i >= 5:
            break
        if 'cover_edition_key' in books and books['cover_edition_key'] != None:
            hasCover = True
            #print(f"cover id : {books['cover_edition_key']}")
            #downloadCovers(books['cover_edition_key'])
            
        if 'author_name' not in books or books['author_name'] == None or books['author_name'] == []:
            #print('Livre: ' + str(books['title']) + ' et pas d\'auteur')
            liste_livre.append(Livre(str(books['title'])))
            #print(liste_livre[i].toString())
            texte = searchUi.answerLabel.text() + str(liste_livre[i].toString())
            searchUi.answerLabel.setText(texte)
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        else:
            #print('Livre: ' + str(books['title']) + ' par l\'auteur ' + str(books['author_name'][-1]) )
            liste_livre.append(Livre(str(books['title'])))
            liste_livre[i].setAuthor(str(books['author_name'][-1]))
            #print(liste_livre[i].toString())
            texte = searchUi.answerLabel.text() + str(liste_livre[i].toString())
            searchUi.answerLabel.setText(texte)
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        hasCover = False


app = QtWidgets.QApplication([])
searchUi = uic.loadUi("ui/search.ui")
searchUi.pushButtonSearch.clicked.connect(searchOpenLibrary)
searchUi.show()
app.exec()