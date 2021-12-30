import requests
import json
from Livre import Livre


search = input("Rentre un livre a rechercher: ")
# Making a get request
response = requests.get(f'https://openlibrary.org/search.json?q={search}&&mode=everything')
#print(response.text)
# print response
#print(response)

# print json content
#print(response.json())

fileToWrite = open('answer.json', 'w+') #Ecrire la reponse au format json dans un fichier json
fileToWrite.write(response.text)
fileToWrite.close()

data = json.loads(response.text) #Transformer le texte en objet json

#print(data)
i = 0
liste_livre = []
for books in data['docs']:
    if i > 5:
        break
    if 'author_name' not in books or books['author_name'] == None or books['author_name'] == []:
        #print('Livre: ' + str(books['title']) + ' et pas d\'auteur')
        liste_livre.append(Livre(str(books['title'])))
        print(liste_livre[i].toString())
        i += 1
    else:
        #print('Livre: ' + str(books['title']) + ' par l\'auteur ' + str(books['author_name'][-1]) )
        liste_livre.append(Livre(str(books['title'])))
        liste_livre[i].setAuthor(str(books['author_name'][-1]))
        print(liste_livre[i].toString())
        i += 1
