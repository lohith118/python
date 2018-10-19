import sys, string, math
s1,s2 = input().split()
L = []
n1 = len(s1)
n2 = len(s2)
if n1 <= n2 :
	for i in range(n1-1,-1,-1) :
		for j in range(0,n1-i) :
			i1 = j
			i2 = j+i+1
			s3 = s1[i1:i2]
			if s3 in s2 :
				print(s3)
				sys.exit()
else  :
	for i in range(n2-1,-1,-1) :
		for j in range(0,n2-i) :
			i1 = j
			i2 = j+i+1
			s3 = s2[i1:i2]
			if s3 in s1 :
				print(s3)
				sys.exit()


