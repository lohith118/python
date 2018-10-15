import sys,string, itertools
n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(1,n) :
    L2.append(max(L[i:]))
L2.append(0)
print(*L2)



