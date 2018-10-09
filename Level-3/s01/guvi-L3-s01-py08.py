import sys, string, math
n = int(input())
L = list(map(int,input().split()))
L2 = []
len1 = len(L)
for i in range(0,len1-2) :
    for j in range(i+1,len1-1) :
        for k in range(j+1,len1) :
            if L[i]+L[j] == L[k] :
                print(L[i],L[j],L[k] )
