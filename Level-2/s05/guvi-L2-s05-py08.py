import sys,string, math,itertools

n = int(input())
L = []
for i in range(1,n) :
    if n%i == 0 :
        L.append(i)
if len(L) > 1 :
    print(*L)
else :
    print(1,n)