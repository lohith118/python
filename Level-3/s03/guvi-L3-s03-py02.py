import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
#print(L)
p = 1
for i in range(0,n) :
    p *= L[i]
L2 = []
for i in range(0,n) :
    a = p // L[i]
    L2.append(a)
print(*L2)