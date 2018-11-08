import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]

L3 = []
for x in L :
    if L.count(x) == k :
        L3.append(x)
        while x in L :
            L.remove(x)
print(*L3)