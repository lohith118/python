import sys,string, math,itertools

s = input()
s2 = ''
for i in range(0,len(s),2) :
    c = s[i]
    n = int(s[i+1])
    s2 += c * n
print(s2)