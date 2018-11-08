import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L1 = [ int(x) for x in input().split()]
L3 = [x for x in L1 if x < k]
L3.sort()

print(*L3)