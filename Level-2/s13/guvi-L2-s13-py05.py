import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]

for x in range(1, min(L)+1) :
      L2 = [ not i%x for i in L]
      #print(x,L2)
      if all(L2) :
            hcf1 = x
print(hcf1)






