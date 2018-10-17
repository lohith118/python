import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
flag = 0
for i in range(1,n-1) :
    sum1 = sum(L[:i])
    sum2 = sum(L[i+1:])
    if sum1 == sum2 :
        flag = 1
        break

if flag == 0 : print('no')
else :         print('yes')