import sys,string, math,itertools
n,k = input().split()
n,k = int(n),int(k)
cnt = 0
for i in range(n,k+1) :
    a = int(math.sqrt(i))
    if a*a == i :
        cnt += 1
print(cnt)

