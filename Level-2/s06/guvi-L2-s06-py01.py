import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
#print(L)
L.sort()
L2 = []
for x in L :
    if x not in L2 :
        L2.append(x)
print(L[1])