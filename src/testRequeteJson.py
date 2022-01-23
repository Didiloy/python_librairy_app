import requests
import urllib.request
import json
import os
from classes.Auteur import Auteur
from classes.Livre import Livre
from classes.Bibliotheque import Bibliotheque

bib = Bibliotheque().getInstance()  # Initialiser la bibliotheque
# bib.initBibliotheque()

#https://covers.openlibrary.org/b/olid/OL26855580M-M.jpg    cover link

def downloadCovers(id, name):
    # url = f'https://covers.openlibrary.org/b/olid/{id}-M.jpg'
    url = id
    pathToImg = os.path.join("..", "assets", "img", name)
    urllib.request.urlretrieve(url, pathToImg) #télécharger l'image

def getJsonGoogleBooksApi(search):
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search}&printType=books')
    answerJson = os.path.join("..", "answer.json")
    fileToWrite = open(answerJson, 'w+')  # Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text)  # Transformer le texte en objet json
    for books in data['items']:
        volumeInfo = books['volumeInfo']
        if 'imageLinks' in volumeInfo and volumeInfo['imageLinks'] != None :
            coversLink = volumeInfo['imageLinks']
            downloadCovers(coversLink['thumbnail'], books['id'])
        print(volumeInfo['title'])
        print(volumeInfo['authors'][0])
        print(books['id'])
        print("\n")

def populateBiblio(search):
    response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything&has_fulltext=true&limit=27')
    answerJson = os.path.join("..", "answer.json")
    fileToWrite = open(answerJson, 'w+')  # Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text)  # Transformer le texte en objet json
    i = 0
    liste_livre = []
    for books in data['docs']:
        livre = Livre(str(books['title']))
        if 'cover_edition_key' in books and books['cover_edition_key'] != None:
            livre.setCoverID(books['cover_edition_key'])
            downloadCovers(books['cover_edition_key'])
        if 'author_name' in books and books['author_name'] != None:
            livre.setAuthor(str(books['author_name'][-1]))
        if 'publish_date' in books and books['publish_date'] != None:
            livre.setDateDeParution(str(books['publish_date'][0]))
        # print(livre)
        bib.addBook(livre)
    bib.writeToJSONFile()

def globalSearch(search):
    # Making a get request
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search}&printType=books')
    answerJson = os.path.join("..", "answer.json")
    fileToWrite = open(answerJson, 'w+')  # Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text)  # Transformer le texte en objet json
    i = 0
    liste_livre = []
    hasCover = False
    for books in data['items']:
        volumeInfo = books['volumeInfo']
        if 'imageLinks' in volumeInfo and volumeInfo['imageLinks'] != None:
            coversLink = volumeInfo['imageLinks']
            hasCover = True

        if 'authors' not in volumeInfo or volumeInfo['authors'] == None or volumeInfo['authors'] == []:
            liste_livre.append(Livre(str(volumeInfo['title'])))
            if hasCover:
                liste_livre[i].setCoverID(str(books['id']))  # je met l'id du livre comme id de cover
                liste_livre[i].setCoverLink(coversLink['thumbnail'])
            i += 1
        else:
            liste_livre.append(Livre(str(volumeInfo['title'])))
            liste_livre[i].setAuthor(str(volumeInfo['authors'][0]))
            liste_livre[i].setHasAuthor(True)
            if hasCover:
                liste_livre[i].setCoverID(str(books['id']))
                liste_livre[i].setCoverLink(coversLink['thumbnail'])
            if 'publishedDate' in volumeInfo and volumeInfo['publishedDate'] != None:
                liste_livre[i].setDateDeParution(volumeInfo['publishedDate'])
            i += 1
        hasCover = False


def authorSearch(search):
    response = requests.get(f'https://openlibrary.org/search/authors.json?q={search}&mode=everything')
    answerJson = os.path.join("..", "answer.json")
    fileToWrite = open(answerJson, 'w+') #Ecrire la reponse au format json dans un fichier json
    fileToWrite.write(response.text)
    fileToWrite.close()
    data = json.loads(response.text) #Transformer le texte en objet json
    i = 0
    for datas in data['docs']:
        if i >= 1:
            break
        if 'birth_date' not in datas:
            auteur = Auteur(str(datas['name']))
            print(auteur.toString())
            bib.addAuthor(auteur)  # Ajouter l'auteur a la bibliotheque
            
        else:
            auteur = Auteur(str(datas['name']))
            auteur.setDateDeNaissance(str(datas['birth_date']))
            print(auteur.toString())
            bib.addAuthor(auteur)  # Ajouter l'auteur a la bibliotheque
        print(f"top work: {datas['top_work']}")
        i += 1
    bib.writeToJSONFile()
def main():
    print("que voulez vous rechercher ?")
    print("-"*20)
    print("1.livre\n2.auteur\n3. remplir la bibliotheque\n4. réinitialiser la bibliotheque\n5. rechercher avec google books")
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
    elif choix == '3':
        print("remplir avec quel livre")
        search = input()
        populateBiblio(search)
    elif choix == '4':
        bib.reinitBib()
    elif choix == '5':
        print("rechercher quel livre")
        search = input()
        getJsonGoogleBooksApi(search)
    #bib.toString()

main()