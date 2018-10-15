import sys,string, itertools
n = int(input())
L = [ int(x) for x in input().split()]
i1 = L.index(min(L))
i2 = L.index(max(L))
print(i1+1,i2+1)


