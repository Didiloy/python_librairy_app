import json
class Bibliotheque:
    def __init__(self):
        self.liste_livre = []
        self.liste_auteur = []
        self.liste_genre = []


    def writeToJSONFile(self):
        data = {} #dictionnaire pour ecrire au format json
        data["livres"] = self.liste_livre
        data["auteurs"] = self.liste_auteur
        data["genres"] = self.liste_genre
        filePathNameWExt = "../assets/database/bibliotheque.json"
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)
            
    def initBibliotheque(self):
        fileToRead = open('../assets/database/bibliotheque.json', 'r') #lire si il y a deja des trucs dans la bibliotheque
        data = fileToRead.read()
        fileToRead.close()
        dataInJson = json.loads(data) #Transformer le texte en objet json
        for livre in dataInJson['livres']:
            self.liste_livre.append(livre)
        for auteur in dataInJson['auteurs']:
            self.liste_auteur.append(auteur)
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
            bib.addBook(title)
        elif choix == '2':
            print("le nom de l'auteur ?")
            author = input()
            bib.addAuthor(author)
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
