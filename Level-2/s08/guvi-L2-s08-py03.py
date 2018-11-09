import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]

print(L.index(k)+1)
