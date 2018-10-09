import sys, string, math
n = int(input())
L = list(map(int,input().split()))
for i in L :
    if L.count(i) == 1 : print(i)
