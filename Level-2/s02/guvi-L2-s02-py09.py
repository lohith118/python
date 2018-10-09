import sys, string, math
n = int(input())
m = n
L = []
for i in range( 2,m) :
    if n%i == 0 : L.append(i)
    while n%i == 0 : n //= i
if len(L) == 0 : print(m)
else :           print(*L)


