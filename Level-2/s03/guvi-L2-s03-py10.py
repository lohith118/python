import sys,string, math,itertools

s1,s2,k = input().split()
k = int(k)

cnt = 0
for c in s1 :
    if c not in s2 :
        cnt += 1
for c in s2 :
    if c not in s1 :
        cnt += 1
if k==cnt :
    print('yes')
else :
    print('no')

