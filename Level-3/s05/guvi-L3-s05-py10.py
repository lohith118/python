import sys, string, math

n,k = input().split()
n,k = int(n), int(k)
if k > n : print(0)
elif k == n : print(1)
else :
    a = 0
    while n >= k :
        a += 1
        n -= k
    print(a)
