import sys,string
s = input()
L = [s[0]]
for c in s :
    if c not in L :
        L.append(c)
s2 = ''.join(L)
print(s2)