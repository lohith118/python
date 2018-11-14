import sys, string, math
from itertools import permutations,combinations

n,k = input().split()
n,k = int(n),int(k)
Lw = [ int(x) for x in input().split()]
Lv = [ int(x) for x in input().split()]
dic1 = {}
for i in range(0,n) :
    dic1[Lw[i]] = Lv[i]
L3 = []
for i in range(1,n+1) :
    L2 = list(combinations(Lw,i))
    for x in L2 :
        if sum(x) <= k :
            L3.append(x)
#print(L3)
max1 = 0
for x in L3 :
    sum1 = 0
    for i in x :
        sum1 += dic1[i]
    #print(x,sum1)
    if sum1 > max1 :
        max1 = sum1
print(max1)



