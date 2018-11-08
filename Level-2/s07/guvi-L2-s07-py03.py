import sys,string, math,itertools

n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
L3 = []
for x in L1 :
    if x in L2 :
        L3.append(x)
        while x in L2 :
            L2.remove(x)

print(*L3)