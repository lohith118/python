import sys,string, itertools
n = int(input())
L = [ int(x) for x in input().split()]
n,k = input().split()
n,k = int(n),int(k)
i1 = abs(L.index(n) - L.index(k))
print(i1)
