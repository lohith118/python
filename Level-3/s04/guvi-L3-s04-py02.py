import sys,string, itertools

n = int(input())
L = [ int(x) for x in input().split()]
Li = [i for i in range(0,len(L))]
#print(L,Li)
while len(L) > 1 :
    L2 = []
    L2i = []
    for i in range(1,len(L),2) :
        L2.append(L[i])
        L2i.append(Li[i])
    #print(L2,L2i)
    L = L2[:]
    Li = L2i[:]
print(L[0])
