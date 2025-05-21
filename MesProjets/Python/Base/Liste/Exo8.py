liste = [1, 2, 3, 6, 4, 2, 5, 4, 1]
liste2 = []
for i in liste: 
    if liste.count(i) > 1:
        if i not in liste2:
            liste2.append(i)
        
print(liste2)