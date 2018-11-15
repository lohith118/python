import sys, string, math

L = [ int(x) for x in input().split()]
L.sort()
a,b,c = L
if a+b <= c or a+c <= b or b+c <= a :
    print('no')
elif a*a + b*b == c*c:
    print('yes')
else :
    print('no')