import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
L.sort()

cnt = 0
for i in range(0,n) :
    #print(i+1, L[i], sum(L[:i]),L[i]-sum(L[:i]))
    if L[i]-sum(L[:i]) >= 0 :
        cnt += 1
    else :
        break
print(cnt)