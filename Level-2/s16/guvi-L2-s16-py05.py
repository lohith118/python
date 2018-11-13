import sys,string, math,itertools

a,b = input().split()
a,b = int(a),int(b)
L1 = [ int(x) for x in input().split()]
k = a//2

L2 = sorted(L1[:k]) + sorted(L1[k:],reverse = True)
print(*L2)