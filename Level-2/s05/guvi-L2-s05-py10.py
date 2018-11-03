import sys,string, math,itertools

n = int(input())
for i in range(1,n) :
    if n%i == 0 :
        print('yes')
        sys.exit()
print('no')
