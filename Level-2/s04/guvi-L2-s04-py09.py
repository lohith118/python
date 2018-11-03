import sys,string, math,itertools

n = int(input())
s = bin(n)[2:]
k = s.count('1')
if k == 1 :
    print('yes')
else :
    print('no')
