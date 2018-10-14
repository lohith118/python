import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
max1 = sum([ abs(x) for x in L])
for i in range(0,n-1) :
    for j in range(i+1,n) :
        if abs(L[i]+L[j]) < max1 :
            max1 = abs(L[i]+L[j])
            a,b = L[i],L[j]
print(a,b)
