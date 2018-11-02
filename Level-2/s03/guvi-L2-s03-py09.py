import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = []
for i in range(n,k+1) :
    a = int(math.sqrt(i))
    if a*a == i :
        L.append(i)
print(*L)

