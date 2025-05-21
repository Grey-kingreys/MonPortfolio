class Rectangle:
    nbRec = 0
    def __init__(self, lon, larg):
        self.__lon = lon
        self.__larg = larg
        Rectangle.nbRec = Rectangle.nbRec + 1
        print(f"Nombre des produits: {Rectangle.nbRec}")
    def perimetre(self):
        return (2 * (self.__lon + self.__larg))
    
    def surface(self):
        return (self.__lon * self.__larg)
    
    def affiche(self):
        print(f"La longueur est: {self.__lon} et la largeur est {self.__larg}")
        
    