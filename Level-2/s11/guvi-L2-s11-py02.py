import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = sorted(L)
L3 = []
if n%2==1 :
    i = 0
    j = n//4
    for i in range(0,j) :
        L3.append(L2[i])
        L3.append(L2[-i-1])
    L3.append(L2[n//2])
    for i in range(j,n//2) :
        L3.append(L2[-i-1])
        L3.append(L2[i])
else :
    i = 0
    j = n//4
    for i in range(0,j) :
        L3.append(L2[i])
        L3.append(L2[-i-1])
    for i in range(j,n//2) :
        L3.append(L2[-i-1])
        L3.append(L2[i])
sum1 = 0
#print(L3)
for i in range(0,n-1) :
    a = max(L3[i],L3[i+1])
    #print(a)
    sum1 += a
print(sum1)







