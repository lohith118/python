import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
L1 = L[:]
L2 = []
for i in range(1,n+1) :
    if i in L1 :
        L1.remove(i)
    else :
        L2.append(i)
L1.sort()
L2.sort()
#print(L1,L2)
k = 0
for i in range(0,len(L1)) :
    k += abs(L1[i] - L2[i])
print(k)
