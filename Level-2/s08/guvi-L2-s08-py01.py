import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n-1) :
    L2.append(max(L[i],L[i+1]))
print(*L2)
