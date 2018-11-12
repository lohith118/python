import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
L.sort(reverse=True)
L2 = sorted(L,key=L.count,reverse=True)
#print(L2)
L3 = []
for x in L2 :
    if x not in L3 :
        L3.append(x)
print(*L3)









