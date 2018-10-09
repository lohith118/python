import sys, string, math
n,k = map(int,input().split())
L = list(map(int,input().split()))
L2 = L[-k:] + L[:-k]
print(*L2)