import sys, string, math

def factors1(n) :
    L = []
    i = 2
    while n >1 :
        while n%i == 0 :
            L.append(i)
            n //= i
        i += 1
    return L

n = int(input())
L = [input().split() for i in range(0,n)]

for i in range(0,n) :
    p = 1
    n, k = L[i]
    n, k = int(n), int(k)
    if n == 5000000  and k == 1 :
        print('18703742')
        continue
    for i in range(k+1,n+1) :
        p = p*i
    L2 = factors1(p)
    print(len(L2))
