import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
sum1 = 0
L2 = []
for i in range(0,n) :
    sum1 = sum(L[:i+1])
    if sum1%2==0 :
        L2.append(sum1)
    else :
        L2.append(L[i])
print(*L2)



