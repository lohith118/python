import sys, string, math
n = int(input())
L = list(map(int,input().split()))
L2 = []
for i in range(0,len(L)) :
    if (i+1)%2 == 1 :
        if L[i] %2 == 1 :
            L2.append(L[i])
    else :
        if L[i] %2 == 0 :
            L2.append(L[i])
print(*L2)