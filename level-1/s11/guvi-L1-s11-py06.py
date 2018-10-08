import sys, string
n,k = map(int,input().split())
L = list(map(int,input().split()))
L2 = [ x for x in L if x%2==1]
print(L2[k-1])
