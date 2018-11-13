import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
k = n//2
L2 = sorted(L[:k]) + sorted(L[k:],reverse=True)
print(*L2)




