import sys,string, math,itertools

s,k = input().split()
k = int(k)
L = []
for i in range(k-1, len(s),k) :
    L.append(s[i])
print(*L)