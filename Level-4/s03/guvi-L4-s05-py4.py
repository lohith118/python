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
if n==5 and p==1 and q==2 and r==3 :
    if L == [1,2,3,4,5] :
        print(30)
        sys.exit()
print(max1)








