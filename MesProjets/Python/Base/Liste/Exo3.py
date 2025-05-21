liste = []
for i in range(5):
    nb = int(input("Donnez un nombre entier: "))
    liste.append(nb)
print(liste[:])
print(sum(liste))
nbElem = 0
for n in liste:
    nbElem = nbElem + 1
print(nbElem)

    