import sys, string, math
n,k = map(int,input().split())
k = k%n
L = list(map(int,input().split()))
L2 = L[-k:] + L[:-k]
print(*L2)
