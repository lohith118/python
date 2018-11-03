import sys,string, math,itertools

n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = sorted(L1)
if L1 == L2 :
    print('yes')
else :
    print('no')