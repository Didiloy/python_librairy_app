class Livre:
    def __init__(self, titre):
        self.titre = titre   # str
        self.auteur  = None# Auteur
        self.isbn = None  # int
        self.genre = None           # str
        self.editeur = None         # Editeur
        self.dateDeParution = None  # datetime

    def setAuthor(self, author):
        self.auteur = author

    def setIsbn(self, isbn):
        self.isbn = isbn

    def setGenre(self, genre):
        self.genre = genre

    def setEditeur(self, editeur):
        self.editeur = editeur

    def setDateDeParution(self, dateDeParution):
        self.dateDeParution = dateDeParution

    def getAuthor(self):
        return self.author

    def getIsbn(self):
        return self.isbn

    def getGenre(self):
        return self.genre

    def getEditeur(self):
        return self.editeur

    def getDateDeParution(self):
        return self.dateDeParution

    def toString(self):
        print(f" Titre : {self.titre}\n Auteur : {self.auteur}")
