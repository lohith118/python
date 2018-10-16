import sys,string
s = input()
L = []
L.append(s[0])
for i in range(1,len(s)) :
    if s[i] not in L :
        L.append(s[i])
s2 = ''.join(L)
print(s2[::-1])



