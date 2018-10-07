import sys, string, math
n = int(input())
for i in range(1,n+1) :
    a = int(input())
    if a != i :
        print(i)
        break
'''
L = list(map(int,input().split()))
for i in range(len(L)) :
    if L[i] != i+1 :
        print(i+1)
        break
'''
