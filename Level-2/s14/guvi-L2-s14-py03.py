import sys,string, math,itertools

n,k = input().split()
n,k = int(n),int(k)
for i in range(0,n) :
    a,b = input().split()
    a,b = int(a), int(b)
    if a <= k <= b :
        print('yes')
        sys.exit()
print('no')

