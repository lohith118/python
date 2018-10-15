import sys,string

n = int(input())
L = []
for i in range(0,n) :
    L.append([])
#print(L)
sum1 = 0
for i in range(0,n) :
    L[i] = [int(x) for x in input().split()]
    sum1 += sum(L[i])
av = sum1 / (n*n)
print('%.6f'%av)
