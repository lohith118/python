import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
n = len(L)
L2 = []
for i in range(0,n) :
    cnt = 1
    if L[i] > 0:
        flag = 1
    else:
        flag = -1
    for j in range(i+1,n) :
        if L[j] > 0:
            if flag == 1 :
                break
            else :
                cnt += 1
                flag = 1
        else:
            if flag == -1 :
                break
            else :
                cnt += 1
                flag = -1
    L2.append(cnt)
print(*L2)







