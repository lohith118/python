import sys, string, math, itertools
n,m = list(map(int,input().split()))
L = []

for i in range(0,n) :
    L.append([])
for i in range(0, n):
    L[i] = list(map(int, input().split()))
for i in range(0,n) :
    if L[i].count(0) > 0 :
        L[i] = [0 for x in range(m)]
for i in range(0,n) :
    for j in range(0,m-1) :
        print(L[i][j],end=' ')
    print(L[i][m-1])

