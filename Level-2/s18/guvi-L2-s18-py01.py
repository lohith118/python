import sys,string, math,itertools

def windex(L1,s2) :
    L1 = s.split()
    L2 = []
    while s2 in L1 :
        i = L1.index(s2)
        L2.append(i)
        L1[i] = ' '
    return L2

s =input()
L = s.split()
if len(L)==1 or L.count('and')==0 :
    print(s)
    sys.exit()
L2 = windex(s,'and')
for i in L2 :

    L[i-1],L[i+1] = L[i+1],L[i-1]
print(*L)

