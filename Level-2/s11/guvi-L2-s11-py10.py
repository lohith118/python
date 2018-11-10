import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
if n==1 :
    print(L[0])
    sys.exit()
for i in range(0,n) :
    L2.append(sum(L[i:]) + sum(L[:i+1]))
print(*L2)










