import sys, string, math
n,a,b = input().split()
n,a,b = int(n), int(a), int(b)
if n % (a+b) == 0 :
    print('YES')
else :
    print('NO')



