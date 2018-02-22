#sum of k nos of n nos
import sys
n,k = map(int,input('enter n,k : ').split())
L = list(map(int,input('enter n nos : ').split()))
sum = 0
for i in range(k) :
    sum += L[i]
print(sum)

