nb = int(input("Donner un nombre entier: "))
liste = []
for i in range(nb):
    if(i >= 1):
        if(nb % i == 0):
            liste.append(i)
    i = i + 1

print(liste)