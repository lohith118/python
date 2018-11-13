import sys,string, math,itertools

a,b = input().split()
a,b = int(a),int(b)
c = a * b
s = bin(c)[2:]
k = s.count('1')

print(k)