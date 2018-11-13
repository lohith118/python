import sys,string, math,itertools

a,b = input().split()
a,b = int(a),int(b)
c = a * b
s = bin(c)[2:]
s2 = s[::-1]
k = s2.index('1') + 1
print(k)