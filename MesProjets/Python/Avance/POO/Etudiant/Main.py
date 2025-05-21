import pickle

class date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        return f"{self.jour}/{self.mois}/{self.annee}"

class Etudiant:
    matricule = 0
    def __init__(self, nom, prenom, filiere, date):
        self.nom = nom
        self.prenom = prenom
        self.filiere = filiere
        self.dateN = date
        self.matricule = Etudiant.matricule + 1

    def __str__(self):
        return f"Matricule: {self.matricule} \nNom: {self.nom}\nPrenom: {self.prenom} \nFiliere: {self.filiere} \nDate de naissaice: {self.dateN}"


input("Appuyer sur une touche pour quitter....")

