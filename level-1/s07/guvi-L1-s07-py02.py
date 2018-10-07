import sys, string
n = int(input())
flag = 1
while n :
    a = n%10
    if not ( a == 0 or a == 1) :
        flag = 0
        break
    n //= 10
if flag : print('yes')
else :    print('no')





