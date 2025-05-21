Prix = float(input("Donnez le prix du produit: "))
TVA = float(input("Donnez le % de la TVA: "))
TTC = Prix + ((Prix * TVA)/100)
print(f"Le montant TTC de ce produit est de: {TTC}")