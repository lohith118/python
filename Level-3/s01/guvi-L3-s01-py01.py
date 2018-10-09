import sys, string, math
n = int(input())
L = list(map(int,input().split()))
dic1 = {}
for i in L :
    if i in dic1 :
        dic1[i] += 1
    else :
        dic1[i] = 1
L = []
flag = 1
for k in dic1 :
    if dic1[k] > 1 :
        L.append(k)
        flag = 0
if flag : print('unique')
else : print(*sorted(L))

