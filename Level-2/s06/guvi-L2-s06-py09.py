import sys, string, math
L =  list(input())

L2 = []
L3 = L[:]
#print(L3)
while L3.count('0') > 0 :
    k = L3.index('0')
    for i in range(0,k) :
        L2.append(L3[i])
    L3 = L3[k+1:]
print(*L2)
