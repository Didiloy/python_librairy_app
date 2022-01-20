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

def downloadCovers(id):
    url = f'https://covers.openlibrary.org/b/olid/{id}-M.jpg'
    pathToImg = os.path.join("..", "assets", "img", id)
    urllib.request.urlretrieve(url, pathToImg) #télécharger l'image

def populateBiblio(search):
    response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything')
    answerJson = os.path.join("answer.json")
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
    response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything')
    answerJson = os.path.join("answer.json")
    fileToWrite = open(answerJson, 'w+') #Ecrire la reponse au format json dans un fichier json
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
    answerJson = os.path.join("answer.json")
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
    print("1.livre\n2.auteur\n3. remplir la bibliotheque\n4. réinitialiser la bibliotheque")
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
    #bib.toString()

main()