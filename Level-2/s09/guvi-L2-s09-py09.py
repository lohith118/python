import sys,string, math,itertools
def fact(n) :
    p = 1
    for i in range(1,n+1) :
        p = p * i
    return p
n,k = input().split()
n,k = int(n),int(k)
ans = fact(n) // fact(n-k)
print(ans)








