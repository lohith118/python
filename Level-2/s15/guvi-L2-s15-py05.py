import sys,string, math,itertools

n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = [ i for i in range(1,n+1)]

L1.sort()
if L1 == L2 :
    print('yes')
else :
    print('no')


