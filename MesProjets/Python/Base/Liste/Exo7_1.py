L1 = [1, 3, 4, 6, 8, 10]
L2 = [1, 2, 4, 5, 7, 9]
L3 = []

for i in L1:
    if i not in L2:
        L3.append(i)
for j in L2:
    if j not in L1:
        L3.append(j)
L3.sort(key= None, reverse= False)

print(L3)
    
