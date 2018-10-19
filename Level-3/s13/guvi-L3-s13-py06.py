import sys, string, math
L = input().split()
flag = 1
for s in L :
    if not ( s[0].isupper()  and s[1:].islower() ) :
        flag = 0
        break
if flag : print('yes')
else :    print('no')




