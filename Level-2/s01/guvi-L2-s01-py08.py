import sys, string, math
s = input()
L = s.split()
L2 = []
for s2 in L :
    L2.append(s2.capitalize())
s3 = ' '.join(L2)
print(s3)
