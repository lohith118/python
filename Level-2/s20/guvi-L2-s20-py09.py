import sys, string, math

s = input()
n = len(s)
k = n//2
cnt = 0
for i in range(0,k) :
    if s[i] != s[-i-1] :
        cnt += 1

if n%2==1 and cnt==1 :
    cnt = 2
if cnt <= 1 :
    print('yes')
else :
    print('no')