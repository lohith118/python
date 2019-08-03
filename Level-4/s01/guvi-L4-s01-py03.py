import sys, string, math
p1,p2 = input().split()
n1 = len(p1)
n2 = len(p2)
if n2 > n1 :
    i = 0
    while i<n1 and p1[i] == p2[i] :
        i += 1
    print(n2-i)
elif n2 == n1 :
    i = 0
    while i<n2 and p1[i] == p2[i] :
        i += 1
    print(n2-i)
else :
    i = 0
    while i<n2 and s1[i] == p2[i] :
        i += 1
    s31 = p1[i:]
    s32 = p2[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n1-i-k)

