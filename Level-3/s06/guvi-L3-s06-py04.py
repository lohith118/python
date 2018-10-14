import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n) :
    min1 = min(L[:i+1])
    L2.append(min1)
print(*L2)

