import sys, string, math

s1,s2 = input().split()

dic1 = {}
dic2 = {}
for c in s1 :
	dic1[c] = dic1.get(c,0) + 1
for c in s2 :
	dic2[c] = dic2.get(c,0) + 1
#print(dic1,dic2)
if dic1.keys() == dic2.keys() :
	print('true')
else :
	print('false')

