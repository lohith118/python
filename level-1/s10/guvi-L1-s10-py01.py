import sys, string, math
a,b,c = map(int,input().split())
area = 2 * (a*b + a*c + b*c)
vol = a * b * c
print(area,vol)
