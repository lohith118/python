import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
L.sort(reverse = True)
print(L)
k = n//2
if n %2 == 0 :
	for i in range(0,k) :
		L2.append(L[i])
		L2.append(L[-i-1])
else :
	for i in range(0,k) :
		L2.append(L[i])
		L2.append(L[-i-1])
	L2.append(L[k])	
print(*L2)
