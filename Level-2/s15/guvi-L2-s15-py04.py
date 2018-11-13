import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(1,n) :
    if L[i] % L[i-1] == 0 :
        L2.append(L[i])
print(*L2)


