import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)

L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
L3 = sorted(L1+L2)
print(*L3)





