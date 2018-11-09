import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
cnt0 = 0
cnt1 = 0
for i in range(0,n) :
    if L[i] %2 == 0 :
        cnt0 += 1
        even = L[i]
    else :
        cnt1 += 1
        odd = L[i]
if cnt0 == 1 :
    print(even)
else :
    print(odd)


