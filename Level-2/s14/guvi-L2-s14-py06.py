import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ int(x) for x in input().split()]
ans = L.count(k)
if ans :
    print('yes',ans)
else :
    print('no')



