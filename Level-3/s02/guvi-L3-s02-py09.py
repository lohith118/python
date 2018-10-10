import sys, string, math, itertools
n,k = map(int,input().split())
L = []

for i in range(0,n) :
    L.append([])
for i in range(0, n):
    L[i] = list(map(int, input().split()))
L2 = L[0][:]
L3 = []
for j in range(1,n) :
    for i in range(0,k) :
        if L[j][i] in L2 :
            L3.append(L[j][i])
            L2.remove(L[j][i])
    #print(L3)
    L2 = L3[:]
    L3 = []
print(*L2)

