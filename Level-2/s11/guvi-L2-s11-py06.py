import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for x in L :
    if x not in L2 :
        L2.append(x)
print(*L2)










