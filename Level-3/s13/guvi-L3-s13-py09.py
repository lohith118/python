import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,len(L)) :
    if L[i] not in L2 :
        L2.append(L[i])
#print(L2)
cnt = 0
for i in range(0,len(L2)) :
    if L.count(L2[i]) > cnt :
        cnt = L.count(L2[i])
        num = L2[i]
print(num)


