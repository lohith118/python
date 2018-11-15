import sys, string, math

s = input()
s1,s2 = s.split()
for c in s1[:] :
	if s.count(c) > 1 :
		s = s.replace(c,c.upper())
		#print(s)

print(s)


