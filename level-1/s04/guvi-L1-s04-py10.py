import sys, string
n = int(input())
L = [1,1]
a,b = 1,1
for i in range(2,n) :
    c = a+b
    L.append(c)
    a,b = b,c
print(*L)


