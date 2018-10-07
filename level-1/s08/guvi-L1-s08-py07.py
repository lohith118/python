import sys, string
n = int(input())
L = []
for i in range(1,n+1) :
    if n%i == 0 : L.append(i)
print(*L)
