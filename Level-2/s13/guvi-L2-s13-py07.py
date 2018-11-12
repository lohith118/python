import sys,string, math,itertools

s1 = input()
s2 = input()
L = s1.split()
L2 = [ x for x in L if x != s2]
print(*L2)






