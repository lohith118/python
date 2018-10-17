import sys,string
n = int(input())
sum1 = 0
while n :
    d = n%10
    sum1 += d*d
    n //= 10
print(sum1)











