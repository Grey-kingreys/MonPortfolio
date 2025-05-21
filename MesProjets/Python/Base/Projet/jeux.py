Monstre1 = input("Entrez le nom du 1er monstre: ")
PV1 = int(input("Entrez ces PV: "))
Monstre2 = input("Entrez le nom du 2eme monstre: ")
PV2 = int(input("Entrez ces PV: "))
n1 = len(f"{Monstre1} ({PV1} PV) Affronte {Monstre2} ({PV2} PV)") + 4
print("+"*n1)
print(f"+ {str.capitalize(Monstre1)} ({PV1} PV) Affronte {str.capitalize(Monstre2)} ({PV2} PV) +")
print("+"*n1)
print("++++++++++++++++++++++++++++ 1er tour de jeu ++++++++++++++++++++++++++++++++")
attaque1 = int(input(f"{Monstre1}, combien des degats infligez-vous a {Monstre2}? "))
PV2 = PV2 - attaque1
n2 = len(f"{Monstre1} attaque {Monstre2} qui perd {attaque1} PV") + 4
n2_2 = n2 - len(f"{Monstre2} a maintenant {PV2} PV") - 5
print("+" * n2)
print(f"+ {Monstre1} attaque {Monstre2} qui perd {attaque1} PV +")
print(f"+ {Monstre2} a maintenant {PV2} PV {" "* n2_2} +")
print("+" * n2)
attaque2 = int(input(f"{Monstre2}, combien des degats infligez-vous a {Monstre1}? "))
PV1 = PV1 - attaque2
n3 = len(f"{Monstre2} attaque {Monstre1} qui perd {attaque2} PV") + 4
n3_2 = n3 - len(f"{Monstre1} a maintenant {PV1} PV") - 5
print("+" * n3)
print(f"+ {Monstre2} attaque {Monstre1} qui perd {attaque2} PV +")
print(f"+ {Monstre1} a maintenant {PV1} PV {" "* n3_2} +")
print("+" * n3)
n4_1 = len(f"Resultat du combat: ") + 4
n4_2 = len(f"{Monstre1} a {PV1} PV")
n4_3 = len(f"{Monstre2} a {PV2} PV")
print("+" * n4_1)
print(f"+ Resultat du combat: +")
print(f"+ {Monstre1} a {PV1} PV {" " * (n4_1 - n4_2 - 4)} +")
print(f"+ {Monstre2} a {PV2} PV {" " * (n4_1 - n4_3 - 4)} +")
print("+" * n4_1)
