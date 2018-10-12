import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
L2 = L[::-1]
L3 = [str(x) for x in L2]
s = '->'.join(L3)
print(s)
