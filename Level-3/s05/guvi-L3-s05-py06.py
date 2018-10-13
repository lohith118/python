import sys,string, itertools
n = int(input())
L = [ int(x) for x in input().split()]
cnt = 0
for i in range(0,n) :
    k = (i+1) * L[i]
    if k in L :
        cnt += 1
print(cnt)
