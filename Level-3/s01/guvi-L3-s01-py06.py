import sys, string, math
n = int(input())
L = list(map(int,input().split()))
flag = 1
for i in range(len(L)) :
    if L.count(L[i]) > 1 :
        print(L[i])
        flag = 0
        break
if flag == 1 : print('unque')


