import sys, string, math
n = int(input())
L1 = [ int(x) for x in input().split()]
L2= [ int(x) for x in input().split()]
L3 = []
for i in range(0,n) :
    L3.append(L1[i]+L2[i])
print(*L3)