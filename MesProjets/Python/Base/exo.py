seconde = int(input("Donnez un temps en seconde: "))
h = seconde // 3600
r1 = seconde % 3600
m = r1 // 60
s = r1 % 60
print(f"{seconde}s donne {h} heures {m} minutes {s} secondes")