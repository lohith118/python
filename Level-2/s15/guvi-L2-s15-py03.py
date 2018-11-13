import sys,string, math,itertools

n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
L22 = sorted(L2)
L12 = []
for x in L22 :
    k = L2.index(x)
    L12.append(L1[k])
print(*L12)

