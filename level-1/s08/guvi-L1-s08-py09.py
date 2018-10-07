import sys, string, math
a,b = map(int,input().split())
p = math.sqrt(a * b)

if p == int(p) : print('yes')
else :           print('no')

