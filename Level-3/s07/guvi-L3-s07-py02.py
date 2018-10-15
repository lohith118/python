import sys,string, itertools
n = int(input())
L = [ int(x) for x in input().split()]
min1 = min(L[:-1])
i1 = L.index(min1)
max1 = max(L[i1+1:])
print(max1-min1)



