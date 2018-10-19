import sys, string, math
s = input()
L = list(s)
L2 = []
for i in range(0,len(L)) :
    if L[i] not in L2 :
        L2.append(L[i])
#print(L2)
L3 = []
for i in range(0,len(L2)) :
    if L.count(L2[i]) == 1 :
        L3.append(L2[i])
s2 = ''.join(L3)
print(s2)


