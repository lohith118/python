import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
sum1 = 0
# increasing len from 1 to n
for j in range(0,n) :
    #print('arr len = ', j+1)
    for i in range(0,n-j) :
        li, ri = i,j+i
        #print(li, ri, L[li:ri+1])
        sum2 = sum(L[li:ri+1])
        if sum2 < sum1 :
            sum1 = sum2
print(sum1)


