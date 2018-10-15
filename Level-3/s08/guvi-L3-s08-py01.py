import sys,string
L = input().split()
n = len(L)
L2 = []
for i in range(0,n) :
    if (i+1)%2 == 1 :
        L2.append(L[i][::-1])
    else :
        L2.append(L[i])
print(*L2)
