import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
a,b = max(L), min(L)
k = abs(L.index(a) - L.index(b))
print(k)
