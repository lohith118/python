import sys,string, math,itertools

n = int(input())
L = [ input() for i in range(0,n)]
vow = 'aeiou'
flag = True
for s in L :
    k = 0
    for c in vow :
        if c in s :
            k += 1
    if k == 0 :
        print('no')
        sys.exit()
print('yes')