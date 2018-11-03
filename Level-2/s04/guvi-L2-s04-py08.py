import sys,string, math,itertools

n = int(input())
L = []
for i in range(2,n+1,2) :
    if n%i == 0 :
        L.append(i)
print(*L)

