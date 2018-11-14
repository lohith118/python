import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
if k in L :
    print(k)
else :
    L2 = [x for x in L if x < k]
    print(max(L2))