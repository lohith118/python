import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
ans = L[0]
for i in range(1,n) :
    ans = ans | L[i]
print(ans)







