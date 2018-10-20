import sys, string, math
n,k = input().split()
n,k = int(n), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,n) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum(L[a-1:b]))




