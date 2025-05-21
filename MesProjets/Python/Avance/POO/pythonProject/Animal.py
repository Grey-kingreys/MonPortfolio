class animal:
    def __init__(self, nom):
        self.nom = nom
    def estVivant(self):
        print(f"{self.nom} est vivant....")
    def se_deplacer(self):
        print(f"{self.nom} se deplace...")
    def affiche(self):
        print(f"{self.nom} est animal")

class Carnivor(animal):
    def __init__(self, nom, demainDeDeplacement):
        print("Creation d'un animal Carnivor")
        animal.__init__(self,nom)
        self.domainDeplacement = demainDeDeplacement
    def se_deplacer(self):
        print(f"{self.nom} se deplace sur {self.domainDeplacement}")
    def se_nourir(self):
        print(f"{self.nom} se nourir de la viande")
    def affiche(self):
        print(f"{self.nom} est un animal carnivor")

#Progamme principale
A1 = animal("Lion")
A1.affiche()
A1.estVivant()
A1.se_deplacer()
A2 = Carnivor("Requin", "La mer")
A2.affiche()
A2.estVivant()
A2.se_deplacer()
A2.se_nourir()

print("Teste")
if(isinstance(A1, animal)):
    print(f"{A1.nom} est un animal")
if(issubclass(Carnivor, animal)):
    print(f"La classe {Carnivor} est une classe fille de la classe {animal}")




