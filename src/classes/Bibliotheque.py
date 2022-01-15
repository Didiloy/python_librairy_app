import json
from classes import Livre
from classes import Auteur
class Bibliotheque:
    def __init__(self):
        self.liste_livre = []
        self.liste_auteur = []
        self.liste_genre = []


    def writeToJSONFile(self):
        data = {} #dictionnaire pour ecrire au format json
        # data["livres"] = for livre in self.liste_livre: livre.addToBib()
        data["livres"] = []
        data["auteurs"] = []
        data["genres"] = []
        for livre in self.liste_livre:
            # print(f"{livre} : {livre.addToBib()}")
            data["livres"].append(livre.addToBib())
        for auteur in self.liste_auteur:
            data["auteurs"].append(auteur.addToBib())
        for genre in self.liste_genre:
            data["genres"].append(genre)
        filePathNameWExt = "../assets/database/bibliotheque.json"
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)
        print("saved")    
        
    def initBibliotheque(self):
        fileToRead = open('../assets/database/bibliotheque.json', 'r') #lire si il y a deja des trucs dans la bibliotheque
        data = fileToRead.read()
        fileToRead.close()
        dataInJson = json.loads(data) #Transformer le texte en objet json
        for books in dataInJson['livres']: # Transformer les livres lus en objets
            #####################################################
            livre = Livre.Livre(str(books['title']))
            if 'coverId' in books and books['coverId'] != None:
                livre.setCoverID(books['coverId'])
            if 'author' in books and books['author'] != None:
                livre.setAuthor(str(books['author']))
                livre.setHasAuthor(True)
            if 'dateDeParution' in books and books['dateDeParution'] != None:
                livre.setDateDeParution(str(books['dateDeParution']))
            self.liste_livre.append(livre)
            # print(f"{livre} : {livre.addToBib()}")
            #####################################################
        for auteur in dataInJson['auteurs']: # Transformer les auteurs lus en objets
            ###################################################"
            author = Auteur.Auteur(str(auteur['name']))
            if 'dateDeNaissance' in auteur and auteur['dateDeNaissance'] != None:
                author.setDateDeNaissance(str(auteur['dateDeNaissance']))
            # print(f"{author} : {author.addToBib()}")
            self.liste_auteur.append(author)
            #####################################################
        for genre in dataInJson['genres']:
            self.liste_genre.append(genre)
        #print(self.liste_livre)

    def addBook(self, book):
        self.liste_livre.append(book)

    def addAuthor(self, author):
        self.liste_auteur.append(author)

    def addGenre(self, genre):
        self.liste_genre.append(genre)

    def toString(self):
        print(self.liste_livre)
        print(self.liste_auteur)
        print(self.liste_genre)

    def reinitBib(self):
        print("reinitialisation")
        data = {}
        data["livres"] = []
        data["auteurs"] = []
        data["genres"] = []
        filePathNameWExt = "../assets/database/bibliotheque.json"
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)
        print("saved reinit")

    def getListeLivre(self):
        return self.liste_livre

def main():
    bib  = Bibliotheque()
    bib.initBibliotheque()
    boucle = True
    while(boucle):
        print("que voulez vous faire ?")
        print("-"*20)
        print("1.ajouter un livre\n2. ajouter un auteur\n3. ajouter un genre\n4. enregistrer\n5. afficher la bibliotheque\n6. Quitter")
        print("-"*20)
        choix = input()
        if choix == '1' :
            print("quel est le titre ")
            title = input()
            livre = Livre.Livre(title)
            bib.addBook(livre.addToBib())
        elif choix == '2':
            print("le nom de l'auteur ?")
            authorName = input()
            auteur = Auteur.Auteur(authorName)
            bib.addAuthor(auteur.addToBib())
        elif choix == '3' :
            print("quel est le genre ? ")
            genre = input()
            bib.addGenre(genre)
        elif choix == '4' :
            print("merlige ")
            bib.writeToJSONFile()
        elif choix == '5':
            bib.toString()
        elif choix == '6':
            boucle = False

#main()