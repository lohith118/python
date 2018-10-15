import sys,string, itertools
L = []
s = input()
while s != '':
    L.append(s)
    s = input()
#print(L)
n = len(L)
L2 = []
for i in range(0,n) :
    L2.append([])
for i in range(0,n) :
    L3 = L[i].split('#')
    #print(L3)
    tot = 0
    for j in range(1,4) :
        tot += int(L3[j])
    L2[i].append(L3[0])
    L2[i].append(tot)
#print(*L2)
L4 = sorted(L2, key = lambda x : x[1], reverse = True)
#print(*L4)
print(L4[0][0])


