import sys, string, math

s,k = input().split()
k = int(k)
n = len(s)
L =[]
for i in range(0,n-k+1) :
    L.append(s[i:i+k])
print(*L)
