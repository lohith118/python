import sys,string, math, itertools

n = int(input())
L = []
if n==2 :
    print('2 1 2')
    sys.exit()
k = n//2
for i in range(2,n+1,2) :
    L.append(i)
for i in range(1,n,2 ) :
    L.append(i)
for i in range(2,n+1,2 ) :
    L.append(i)
print(*L)


