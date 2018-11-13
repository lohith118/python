import sys,string, math,itertools

s = input()
k = len(s) - s.count('a') -s.count('b')
if k <= 1 :
    print('yes')
else :
    print('no')

