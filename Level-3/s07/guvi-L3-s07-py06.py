import sys,string, itertools

n = int(input())
L = input().split()
s = input()
n2 = len(s)
k = 0
for i in range(0,len(L)) :
    if L[i][:n2] == s :
        k += 1
print(k)


