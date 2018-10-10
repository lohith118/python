import sys, string, math
n,m = map(int,input().split())
L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))
flag = 1
for i in range(0,len(L2)) :
    if L2[i] not in L1 :
        flag = 0
        break
if flag : print('YES')
else :    print('NO')


