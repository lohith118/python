import sys, string, math
s = input()
L = s.split()
print(L)
L2 = []
for s2 in L :
    s3 = s2[0].upper() + s2[1:]
    L2.append(s3)
print(*L2)