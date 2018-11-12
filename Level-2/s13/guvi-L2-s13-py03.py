import sys,string, math,itertools

n = int(input())
L = []
if n==2 or n==3 :
      L.append(n)
else :
      for i in range(2,n) :
            if n%i == 0 and i not in L :
                  L.append(i)
            while n%i == 0 :
                  n = n//i
print(*L)







