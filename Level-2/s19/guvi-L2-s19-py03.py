import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
cnt = 0
for i in range(1,n+1) :
    if i in L :
        L.remove(i)
print(len(L))
