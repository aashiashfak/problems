
ar1= [1, 5, 10, 20, 40, 80] 
ar2 = [6, 7, 20, 80, 100] 
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = []

for i in range(len(ar1)):
    for j in range( len(ar2)):
        if ar1[i] == ar2[j]:
            common.append(ar1[i])
            break

for k in range(len(ar3)):
    if ar3[k] in common:
        print(ar3[k])
                


common_elements = set(ar1) & set(ar2) & set(ar3)

print(common_elements)
