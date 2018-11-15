import sys, string, math

n,k = input().split()
n,k = int(n),int(k)

a = n % k
if a==0 :
    a = k
print(a)
