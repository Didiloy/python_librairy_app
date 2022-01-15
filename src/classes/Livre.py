class Livre:
    def __init__(self, titre):
        self.titre = titre   # str
        self.auteur  = None# Auteur
        self.isbn = None  # int
        self.genre = None           # str
        self.editeur = None         # Editeur
        self.dateDeParution = None  # datetime
        self.coverId = None         #string
        self.hasAuthor = False      #bool

    def setHasAuthor(self, bool):
        self.hasAuthor = bool

    def getHasAuthor(self):
        return self.hasAuthor

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

    def setCoverID(self, coverId):
        self.coverId = coverId

    def getCoverID(self):
        return self.coverId

    def getAuthor(self):
        return self.auteur

    def getIsbn(self):
        return self.isbn

    def getGenre(self):
        return self.genre

    def getEditeur(self):
        return self.editeur

    def getTitre(self):
        return self.titre

    def getDateDeParution(self):
        return self.dateDeParution

    def addToBib(self):
        return {"title": self.titre, "author": self.auteur, "coverId": self.coverId, "genre": self.genre, "editeur": self.editeur, "dateDeParution": self.dateDeParution, "hasAuthor": self.hasAuthor}
        #[self.titre, self.auteur, self.coverId,self.genre, self.editeur, self.dateDeParution]

    def toString(self):
        return (f" Titre : {self.titre}\n Auteur : {self.auteur}\n")
