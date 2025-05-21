class Etudiant:
    nb_Etudiant = 0
    def __init__(self, nom, note1, note2):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2

    def cal_moy(self):
        return (self.note1 + self.note2)/2
    def Afficher(self):
        print(f"Bonjour Monsieur {self.nom}")
        print(f"Vous avez la moyenne: {self.cal_moy()}")

    """Programme de test"""

while True:
    try:
        nom = input("Donnez votre nom complet: ")
        if nom.isdigit():
            raise ValueError("Donnez un nom en chaine des caractere: ")
        break
    except ValueError as e:
        print(f"Erreur: {e}")
while True:
    try:
        note1 = float(input("Donnez votre premiere note: "))
        break
    except ValueError:
        print("Erreur donnez une note en nombre: ")
while True:
    try:
        note2 = float(input("Donnez votre deuxieme note note: "))
        break
    except ValueError:
        print("Erreur donnez une note en nombre: ")


e1 = Etudiant(nom, note1, note2)
e1.Afficher()

