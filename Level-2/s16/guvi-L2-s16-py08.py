import sys,string, math,itertools

a,b = input().split()
a,b = int(a),int(b)
c = a * b
s = bin(c)[2:]
k = s.index('1') + 1
s2 = s[k:]
k = k + s2.index('1') + 1
print(k)