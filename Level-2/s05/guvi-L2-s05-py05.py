import sys,string, math,itertools

n,k = input().split()
p,a = int(n),int(k)
for b in range(1,p) :
    if 2 * (b + a//b) == p :
        print('yes')
        sys.exit()
print('no')