import sys,string, math,itertools

n,k,c = input().split()
n,k,c = int(n),int(k),int(c)
p = (n**k) % c
print(p)


