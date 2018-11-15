import sys, string, math

n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
if L1 == L2[::-1] :
    print('yes')
else :
    print('no')