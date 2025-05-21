class livre:
    Nb_Livre = 0
    def __init__(self, titre, auteur, prix):
        print("Enregistrement d'un livre...")
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        livre.Nb_Livre += 1

    def Affiche(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Prix: {self.prix} GNF")
        print(f"Nombre des livres enregistrer: {livre.Nb_Livre}")

print(f"Bonjour et bienvenue! Veillez entrez les informations du livre a enregister")
while True:
    try:
        Titre = input("Titre: ")
        if Titre.isdigit():
            raise ValueError("Entrez une chaine de caractere: ")
        break
    except ValueError as e:
        print(f"Erreur: {e}. Veuillez reessayez")
while True:
    try:
        Auteur = input("Auteur: ")
        if Auteur.isdigit():
            raise ValueError("Entrez un nom valide: ")
        break
    except ValueError as s:
        print(f"Erreur: ;{s}. Veuillez reessayez")

while True:
    try:
        prix = float(input("Prix: "))
        break
    except ValueError:
        print("Erreur: Entrez un prix valide: ")

L1 = livre(Titre,Auteur,prix)
L1.Affiche()