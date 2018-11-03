import sys,string, math

n,k = input().split()
n,k = int(n),int(k)
L2 = [ int(x) for x in input().split()]
#print(L)
for i in range(0,n-1) :
    for j in range(i+1,n) :
        if L2[i] > L2[j] :
            L2[i], L2[j] = L2[j], L2[i]
print(*L2)