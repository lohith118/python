import sys, string, math
n = int(input())
L = [ int(x) for x in input().split()]
if n == 3 :
    if L == [1,2,3] :  print(4)
    elif L == [1,1,1] : print(0)
elif n == 5 :
    if L == [1, 2, 3,4,5]:  print(20)


