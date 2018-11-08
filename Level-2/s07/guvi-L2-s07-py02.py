import sys,string, math,itertools

n = int(input())
if n %2 == 1 :
    print(1)
    sys.exit()
for i in range(2,n+1) :
    if n%i == 0 :
        k = n // i
        if k%2 == 1 :
            print(i)
            sys.exit()