import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
L1 = L[:n]
L2 = L[n:]
L3 = []
while len(L1) :
    x = L1[0]
    if x in L2 :
        L3.append(x)
        L1.remove(x)
        L2.remove(x)
    else :
        L1.remove(x)

L3.sort()
print(*L3)











