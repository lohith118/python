import sys,string
n = int(input())
L = [ int(x) for x in input().split()]
L2 = L[::-1]
k = len(L2)
for i in range(0,k-1) :
    print(L2[i],end='->')
print(L[k-1])
