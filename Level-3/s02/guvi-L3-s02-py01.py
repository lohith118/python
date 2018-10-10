import sys, string, math
L = input().split()
L2 = L[::-1]
L3 = []
for s in L2 :
    L3.append(s[::-1])
print(*L3)




