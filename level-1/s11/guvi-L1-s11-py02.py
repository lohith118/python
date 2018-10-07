import sys, string, math
n = int(input())
while n :
    a = n // 2
    if a%2 == 1 :
        print(a)
        break
    n //= 2