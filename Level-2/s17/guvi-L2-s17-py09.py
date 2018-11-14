import sys,string, math,itertools

s = input()
L = []
n = len(s)
i=0
while True :
    c = s[i]
    k = 0
    while i<n and s[i] == c :
        i += 1
        k += 1
    L.append(c)
    L.append(str(k))
    if i==n :
        break
s2 = ''.join(L)
print(s2)