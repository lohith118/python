import sys, string, math
n = int(input())
L = list(map(int,input().split()))
for i in range(len(L)) :
    if L[i] != i+1 :
        print(i+1)
        break

