class PERSONNE:
    PerNum = 0
    age = 0
    def __init__(self, nom, prenom, ville):
        print(f"Creation de l'humain numero: {PERSONNE.PerNum + 1}")
        self.__nom = nom
        self.__prenom = prenom
        self.__ville = ville
        
    @classmethod
    def perso(cls, perso_def):
        __nom, __prenom, __ville = perso_def.split(' ')
        return cls(__nom, __prenom, __age)
