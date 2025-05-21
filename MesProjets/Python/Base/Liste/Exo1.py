jour = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print("Premiere affichement")
for i in jour:
    print(i)
print("Deuxiement affichement")
i = 0
while i  <  len(jour):
    print(jour[i])
    i = i + 1

print("3eme affichement")
print(jour[:])
