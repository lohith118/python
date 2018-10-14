import sys, string, math
n,k = input().split()
n,k = int(n), int(k)
L = [ int(x) for x in input().split()]
L2 = L[k:] + L[:k]
print(*L2)

