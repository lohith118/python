import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
L = [ input() for i in range(0,n)]
vow = 'aeiou'
cnt = 0
for s in L :
    a = 0
    for c in vow :
        if c in s :
            a = 1
            break
    if a > 0 :
        cnt += 1
if cnt >= k :
    print('yes')
else :
    print('no')