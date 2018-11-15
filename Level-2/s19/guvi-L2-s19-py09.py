import sys, string, math

a,b,c = [ int(x) for x in input().split()]
if a+b <= c or a+c <= b or b+c <= a :
    print('no')
elif a==b or a==c or b==c:
    print('no')
else :
    print('yes')