import sys, string, math
n = int(input())
L = list(map(int,input().split()))
L2 = []
len1 = len(L)
min1 = abs(L[0]+L[1])
if min1 == 0:
    print(L[0],L[1])
    sys.exit()
for i in range(0,len1-1) :
    for j in range(i+1,len1) :
        if abs(L[i]+L[j]) < min1 :
            min1 = abs(L[i]+L[j])
            a,b = L[i],L[j]
            if min1 == 0 :
                print(a,b)
                sys.exit()
print(a,b)

