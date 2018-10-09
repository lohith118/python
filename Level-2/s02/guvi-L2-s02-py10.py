import sys, string, math
s = input()
L = []
for c in s :
    k = ord(c) + 3
    if k > ord('Z') : k -= 26
    L.append(chr(k))
s2 = ''.join(L)
print(s2)



