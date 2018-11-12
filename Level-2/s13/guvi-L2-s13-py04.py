import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
for x in range(max(L), max(L)**n,max(L)) :
      L2 = [ not x%i for i in L]
      #print(x,L2)
      if all(L2) :
            print(x)
            sys.exit()






