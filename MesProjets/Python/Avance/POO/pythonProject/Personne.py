class Personne:
    nb_Personne = 0
    def __init__(self, nom, prenom, taille, poids, age):
        print("Verification d'une personne")
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille
        self.poids= poids
        Personne.nb_Personne += 1

    def imc(self):
        return self.poids / (self.taille * self.taille)

    def interpretation(self):
        n = self.imc()
        if(n <= 18):
            print(f"Monsieur {self.prenom} {self.nom} vous avez {self.age} ans avec un imc de {n}. resultat: Insuffisance ponderale")

        elif (n >= 30):
            print(f"Monsieur {self.prenom} {self.nom} vous avez {self.age} avec un imc de {n}. resultat: Obesite")
        else:
            print(f"Monsieur {self.prenom} {self.nom} vous avez {self.age} avec un imc de {n}. resultat: Normal")


print("Veillez fournir vos infomation: ")
while True:
    try:
        prenom = input("Prenom: ")
        if prenom.isdigit():
            raise ValueError("Donnez un nom en chaine de caractere: ")
        break
    except ValueError as e:
        print(f"Erreur {e}")
while True:
    try:
        nom = input("Nom: ")
        if nom.isdigit():
            raise ValueError("Donnez un nom en chaine de caractere: ")
        break
    except ValueError as e:
        print(f"Erreur {e}")
while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print(f"Erreur Donner un age en entier: ")
while True:
    try:
        taille = float(input("Taille (m): "))
        break
    except ValueError:
        print(f"Erreur Donner un taille en reel: ")
while True:
    try:
        poids = float(input("Poids: "))
        break
    except ValueError:
        print(f"Erreur Donner un poids en reel: ")


#Creation d'une personne

P1 = Personne(nom, prenom, taille, poids, age)
P1.interpretation()