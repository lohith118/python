import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
p = 1
for i in range(1,k+1) :
    p = p * i
print(p)