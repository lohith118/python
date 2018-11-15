import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
for i in range(1,n) :
    if i%2 == 1 :
        if L[i] <= L[i-1] :
            print('no')
            sys.exit()
    else :
        if L[i] >= L[i-1] :
            print('no')
            sys.exit()
print('yes')
