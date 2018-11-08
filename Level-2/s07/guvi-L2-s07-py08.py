import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
max1 = 1
x = L[0]
k = 1
for i in range(1,n) :
    if L[i] == L[i-1] :
        k += 1
        if k > max1 :
            max1 = k
    else :
        k = 1
print(max1)