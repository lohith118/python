import sys, string, math

L = input().split()
L2 = []
for s in L :
	L3 = sorted(s)
	s2 = ''.join(L3)
	L2.append(s2)
print(*L2)


