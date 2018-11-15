import sys, string, math
sau = string.ascii_uppercase

s1 = input()
s2 = input()
if len(s1) + len(s2) != 26 :
	print('non-complementary')
	sys.exit()
L = list(s1) + list(s2)
L.sort()
s3 = ''.join(L)
if s3 == sau :
	print('complementary')
else :
	print('non-complementary')

