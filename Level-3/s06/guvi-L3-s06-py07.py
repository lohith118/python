import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
for i in range(0,n) :
    if L.count(L[i]) == 1 :
        print(L[i])
        break