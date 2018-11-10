import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = sorted(L)
L3 = []
for x in L2 :
    L3.append(L.index(x)+1)
print(*L3)










