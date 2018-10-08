import sys, string
n,k = map(int,input().split())
L = list(map(int,input().split()))
L2 = sorted(L)
print(L2[k-1])
