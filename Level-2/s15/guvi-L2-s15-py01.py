import sys,string, math,itertools

n = int(input())
L = [ input() for i in range(0,n)]
#print(L)
for i in range(1,n) :
    if L[i] == L[i-1] :
        print('no')
        sys.exit()
print('yes')
