import sys, string, math
s = input()
L = []
for c in s :
    if c.isdigit() : L.append(c)
print(*L,sep='')
