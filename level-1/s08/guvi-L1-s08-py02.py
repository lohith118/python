import sys, string
s = input()
flag = 0
for c in s :
    if c =='a' or c=='i' or c=='e' or c=='o' or c=='u' :
        flag = 1
        break
if flag : print('yes')
else :    print('no')
