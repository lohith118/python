import sys, string, math
n = int(input())
L = list(map(int,input().split()))
L2 = []
len1 = len(L)
for i in range(0,len1-1) :
    for j in range(i+1,len1) :
        if L[i]+L[j] == 0 :
            print(L[i],L[j])

