import sys, string, math
n = int(input())
a = 0
while n :
    a = a*10 + n%10
    n //= 10
print(a)

