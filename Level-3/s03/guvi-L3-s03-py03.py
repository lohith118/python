import sys,string
from itertools import permutations
def sumL(s,L) :
    #print(s)
    i=0
    j=0
    k = L[i][j]
    for i1 in range(0,len(s)) :
        if s[i1] == 'R' :
            j += 1
            k += L[i][j]
            #print(L[i][j],k)
        else :
            i += 1
            k += L[i][j]
            #print(L[i][j],k)
    return k

n,m = input().split()
n,m = int(n),int(m)
L = []
for i in range(0,n) :
    L.append([])
for i in range(0,n) :
    L[i] = [ int(x) for x in input().split()]

s = 'D'*(n-1) + 'R'*(m-1)
L2 = list(permutations(s))
L3 = [ ''.join(x) for x in L2]
L4 = list(set(L3))
L5 = []
#print(len(L4),L4)
for i in range(0,len(L4)) :
    k = sumL(L4[i],L)
    #print(L4[i],k)
    L5.append(k)
print(max(L5))
