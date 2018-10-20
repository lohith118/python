import sys, string, math

n,p,q,r = input().split()
n,p,q,r = int(n), int(p),int(q), int(r)
#print(n,p,q,r)
L = [ int(x) for x in input().split()]
min1 = min(L)
max1 = min1 *10*n
for i in range(0,n) :
    for j in range(i, n):
        for k in range(j, n):
            pr = p*L[i] + q*L[j] + r*L[k]
            if pr > max1 :
                max1 = pr
print(max1)








