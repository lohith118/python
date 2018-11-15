import sys, string, math

n = int(input())
if n%3==0  or n%7==0 :
    print('yes')
    sys.exit()
a = n%7
if a%3 == 0 :
    print('yes')
    sys.exit()
print('no')

