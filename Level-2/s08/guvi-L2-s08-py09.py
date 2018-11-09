import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
mdiff = abs(L[0]-L[1])
for i in range(0,n-1) :
    for j in range(i+1,n) :
        if abs(L[i]-L[j]) > mdiff :
            mdiff = abs(L[i]-L[j])
print(mdiff)







