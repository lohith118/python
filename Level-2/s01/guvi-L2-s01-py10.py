import sys, string, math
s1, s2 = input().split()
k = 0
for i in range(len(s1)) :
    if s1[i] != s2[i] :
        k += 1
if k == 1 : print('yes')
else :      print('no')