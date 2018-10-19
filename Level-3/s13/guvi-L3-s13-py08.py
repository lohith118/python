import sys, string, math
def isPalin(s) :
	if len(s) == 1 : return False
	if s == s[::-1] : return True

s = input()
L = []
n = len(s)
for i in range(n-1,0,-1) :
	for j in range(0,n-i) :
		i1 = j
		i2 = j+i+1
		s2 = s[i1:i2]
		#print(i1,i2,s2)
		if isPalin(s2) :
			L.append(s2)
L.sort(key = len)
for i in range(0,len(L)) :
	print(L[i])

