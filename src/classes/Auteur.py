class Auteur:
    def __init__(self, nom):
        self.nom = nom                         # str
        self.dateDeNaissance = None # datetime

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getDateDeNaissance(self):
        return self.dateDeNaissance

    def setDateDeNaissance(self, dateDeNaissance):
        self.dateDeNaissance = dateDeNaissance

    def toString(self):
        return f"Nom : {self.nom}\nDate de naissance : {self.dateDeNaissance}"
