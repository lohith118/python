import sys,string, math,itertools

s = input()
ans = len(s) == s.count('a') + s.count('b')
if ans :
    print('yes')
else :
    print('no')


