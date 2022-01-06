import requests
import urllib.request
import json
import os
from classes.Auteur import Auteur
from classes.Livre import Livre


#https://covers.openlibrary.org/b/olid/OL26855580M-M.jpg    cover link

def downloadCovers(id):
    url = f'https://covers.openlibrary.org/b/olid/{id}-M.jpg'
    urllib.request.urlretrieve(url, f"./assets/img/{id}") #télécharger l'image

def globalSearch(search):
    # Making a get request
    response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything')

    fileToWrite = open('src/answer.json', 'w+') #Ecrire la reponse au format json dans un fichier json
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
            print(f"cover id : {books['cover_edition_key']}")
            downloadCovers(books['cover_edition_key'])
            
        if 'author_name' not in books or books['author_name'] == None or books['author_name'] == []:
            #print('Livre: ' + str(books['title']) + ' et pas d\'auteur')
            liste_livre.append(Livre(str(books['title'])))
            print(liste_livre[i].toString())
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        else:
            #print('Livre: ' + str(books['title']) + ' par l\'auteur ' + str(books['author_name'][-1]) )
            liste_livre.append(Livre(str(books['title'])))
            liste_livre[i].setAuthor(str(books['author_name'][-1]))
            print(liste_livre[i].toString())
            if hasCover:
                liste_livre[i].setCoverID(str(books['cover_edition_key']))
            i += 1
        hasCover = False


def authorSearch(search):
    response = requests.get(f'https://openlibrary.org/search/authors.json?q={search}&mode=everything')
    fileToWrite = open('src/answer.json', 'w+') #Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text) #Transformer le texte en objet json
    i = 0
    for datas in data['docs']:
        if i >= 1:
            break
        if 'birth_date' not in datas:
            auteur = Auteur(str(datas['name']))
            auteur.toString()
        else:
            auteur = Auteur(str(datas['name']))
            auteur.setDateDeNaissance(str(datas['birth_date']))
        print(f"top work: {datas['top_work']}")
        i += 1

def main():
    print("que voulez vous rechercher ?")
    print("-"*20)
    print("1.livre\n2.auteur")
    print("-"*20)
    choix = input()
    if choix == '1' :
        print("que voulez vous rechercher ? ")
        search = input()
        globalSearch(search)
    elif choix == '2':
        print("que voulez vous rechercher ?")
        search = input()
        authorSearch(search)
    # bib = Bibliotheque()
    # bib.initBibliotheque()

main()