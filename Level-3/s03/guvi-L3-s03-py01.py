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
    print(*L[i])

