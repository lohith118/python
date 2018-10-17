import sys,string

n = int(input())
L = input().split()
L2 = []
for i in range(0,n) :
    L2.append(L[i].lower())
L2.sort()
print(*L2,sep='\n')











