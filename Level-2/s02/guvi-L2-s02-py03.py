import sys, string, math
n = int(input())
sm = 0
while n :
    a = n%10
    sm = sm + a*a
    n //= 10
print(sm)
