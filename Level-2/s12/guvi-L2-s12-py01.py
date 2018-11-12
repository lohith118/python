import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
L1 = L[:n]
L2 = L[n:]
L3 = []
for x in L1 :
    if x in L2 :
        L3.append(x)
        L2.remove(x)
L3.sort()
print(*L3)











