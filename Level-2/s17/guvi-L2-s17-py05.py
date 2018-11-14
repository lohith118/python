import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
L2 = [x for x in L if x > k]
print(min(L2))