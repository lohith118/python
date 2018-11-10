import sys,string, math,itertools

s,k = input().split()
k = int(k)
for i in range(0,k+1) :
    c = str(i)
    if c not in s :
        print('no')
        sys.exit()
print('yes')





