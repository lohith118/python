import sys, string, math
s = input()
L = list(s)
for i in range(0,len(L),2) :
    L[i],L[i+1] = L[i+1],L[i]
res = ''.join(L)
print(res)

