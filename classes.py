class Editeur:
    def __init__(self, nom):
        self.nom = nom # str

class Auteur:
    def __init__(self, nom, prenom, dateDeNaissance):
        self.nom = nom                         # str
        self.prenom = prenom                   # str
        self.dateDeNaissance = dateDeNaissance # datetime

class Livre:
    def __init__(self, titre, auteur, isbn, genre, editeur, dateDeParution):
        self.titre = titre   # str
        self.auteur = auteur # Auteur
        self.isbn = isbn     # int
        self.genre           # str
        self.editeur         # Editeur
        self.dateDeParution  # datetime
