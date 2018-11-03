import sys,string, math

n = int(input())
L = [ int(x) for x in input().split()]
print(L)
while len(L) > 0 :
    n = len(L)
    if n %2 == 1 :
        k = n//2
        print(L[k])
        L.pop(k)
        #print('odd',L)
    else :
        k = n//2
        print((L[k-1]+L[k])//2)
        L = L[:k-1] + L[k+1:]
        #print('odd',L)








