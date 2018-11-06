import sys, string, math
n,k = input().split()
n,k = int(n), int(k)
L2 = [ int(x) for x in input().split()]
#print(L)
L2.sort()
L3 = []
for x in L2 :
    if x not in L3 :
        L3.append(x)
print(L2[k-1])