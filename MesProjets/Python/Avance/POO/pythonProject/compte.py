class Account:
    def __init__(self, solde = 0):
        self.solde = solde


    def  Getbalance(self):

        return self.solde

    def deposer(self, montant):
        if montant > 0:
            self.solde = self.solde + montant
        else:
            print("Erreur le montant dois etre positive: ")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde = self.solde - montant
        else:
            print("fonds insuffisant")

    def ajout_Interet(self, taux):
        self.solde = self.solde * (1+ taux)

    def affiche(self):
        if hasattr(self, 'solde'):
            print(f"votre solde est: {self.solde}")
        else:
            print("L'attribut solde est manquante")


C1 = Account(500)
C1.ajout_Interet(0.18)
C1.affiche()
C1.retirer(900)
C1.affiche()