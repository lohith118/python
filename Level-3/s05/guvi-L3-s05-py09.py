import sys, string, math
def fact(n) :
    p = 1
    if n == 0 : return 1
    for i in range(1,n+1) :
        p = p * i
    return p

n,k = input().split()
n,k = int(n), int(k)
#print(n,k)
ncr = fact(n)
dn =  fact(n-k) * fact(k)
ncr = ncr // dn
print(ncr)

