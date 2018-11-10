import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = [L[0]]
for i in range(2,n+1) :
    L2.append(sum(L[:i]))
print(*L2)










