import sys, string, math
n = int(input())
L = []
while n :
    a = n%10
    if a%2 == 1 : L.append(a)
    n //= 10
L = L[::-1]
print(*L)

