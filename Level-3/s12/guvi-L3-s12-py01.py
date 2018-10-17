import sys,string

n = int(input())
L = []
for i in range(0,n) :
    L.append([])

for i in range(0,n) :
    L[i] = [int(x) for x in input().split()]
sum1 = 0
for i in range(0,n) :
    sum1 += L[i][i]
print(sum1)













