import sys, string, math
a,b = map(int,input().split())
k = 0
n = b
if b==0 : k = 1
else :
    while n :
        k += 1
        n //= 10
ans = a * 10**k + b
print(ans)
