import sys,string
s = input()
i = 0
n = len(s)
L1 = []
L2 = []
while i<n :
    L1.append(s[i])
    i += 1
    s2 = ''
    while i<n and s[i].isdigit()  :
        s2 = s2 + s[i]
        i += 1
    L2.append(int(s2))

#print(L1,L2)
s2 = ''
for i in range(0,len(L1)) :
    s2 = s2 + L1[i]*L2[i]
print(s2)
