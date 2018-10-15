import sys,string, itertools
n = int(input())
L = [ 1000,500,100,50,10,1]
k = 0
for i in range(0,len(L)) :
    n2 = n // L[i]
    k += n2
    n = n % L[i]
    #print(n2,end=' ')
print(k)



