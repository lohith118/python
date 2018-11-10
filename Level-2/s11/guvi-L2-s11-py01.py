import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
sum1 = 0
for i in range(0,n-1) :
    sum1 += max(L[i],L[i+1])
print(sum1)







