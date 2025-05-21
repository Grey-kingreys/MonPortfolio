dividende = int(input("Donnez un premier entier qui sera le dividende: "))
diviseur = int(input("Donner un entier qui sera le diviseur: "))
q = dividende // diviseur
r =  dividende % diviseur
print(f"La division de {dividende} par {diviseur} donne un quotient de {q} et un reste de {r}")