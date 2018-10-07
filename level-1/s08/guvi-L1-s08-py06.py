import sys, string
n = int(input())
if n==2 : print('no')
else :
    flag = 0
    for i in range(2,n) :
        if n%i == 0 :
           print('yes')
           break
    else :
        print('no')