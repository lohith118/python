import sys,string, math,itertools
n,k = input().split()
n,k = int(n),int(k)
p = k
if n==k :
    print('yes')
    sys.exit()
elif n<k :
    print('no')
    sys.exit()
i = 2
while n >= p :
    p = k**i
    if p==n :
        print('yes')
        sys.exit()
    i += 1
else :
    print('no')
    sys.exit()
