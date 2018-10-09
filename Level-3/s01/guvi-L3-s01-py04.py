import sys, string, math
n = int(input())
L = list(map(int,input().split()))
for i in range(len(L)) :
    if L.count(L[i]) == 1 :
        print(L[i])
        break
