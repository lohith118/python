import sys,string, math,itertools

s,k = input().split()
k = int(k)
L = list(s)
print(L)
for i in range(k-1, len(L),k) :
    L[i] = L[i].upper()

s2 = ''.join(L)
print(s2)