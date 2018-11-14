import sys,string, math,itertools

s = input()
L = []
L2 = [s[0]]
L3 = L2[:]
max1 = s.count(s[0])
for i in range(1,len(s)) :
    c = s[i]
    if c not in L2 :
        L2.append(c)
        k = s.count(c)
        if k > max1 :
            max1 = k
            L3 = [c]
        elif k == max1 :
            L3.append(c)
s2 = ''.join(L3)
print(max1,s2)
