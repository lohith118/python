import sys,string, math,itertools

s,k = input().split()
k = int(k)
n = len(s)
s2 = s[-k:] + s[:-k]
print(s2)