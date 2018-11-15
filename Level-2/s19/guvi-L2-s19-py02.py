import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
cnt = 0
while L :
    k = max(L)
    L.remove(k)
    while k > 0 :
        k -= 1
        if k in L :
            L.remove(k)
    cnt += 1
print(cnt)
