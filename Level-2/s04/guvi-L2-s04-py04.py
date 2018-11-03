import sys,string, math,itertools

s = input()
L = [s[0]]
n = len(s)
for i in range(3,n,3) :
    L.append(s[i])
s2 = ''.join(L)
print(s2)


