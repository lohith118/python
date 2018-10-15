import sys,string

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n-1) :
    if L[i+1] < L[i] :
        L2 .append(L[i+1])
    else :
        L2.append(-1)
L2.append(-1)
print(*L2)
