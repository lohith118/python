import sys,string

s1,s2 = input().split()
n1 = len(s1)
n2 = len(s2)
L = []
if n1 == n2 :
    for i in range(0,n1) :
        L.append(s1[i])
        L.append(s2[i])
elif n1 < n2 :
    for i in range(0,n1) :
        L.append(s1[i])
        L.append(s2[i])
    k = 1
    i += 1
    for j in range(i,n2) :
        L.append(str(k))
        L.append(s2[i])
        k += 1
        i += 1
else :
    for i in range(0,n2) :
        L.append(s1[i])
        L.append(s2[i])
    k = 1
    i += 1
    for j in range(i,n1) :
        L.append(s1[i])
        L.append(str(k))
        k += 1
        i += 1

res = ''.join(L)
print(res)












