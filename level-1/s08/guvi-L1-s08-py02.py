import sys, string
s = input()
s2 = 'aeiouAEIOU'
flag = 0
for c in s :
    if c in s2 :
        flag = 1
        break
if flag : print('yes')
else :    print('no')
