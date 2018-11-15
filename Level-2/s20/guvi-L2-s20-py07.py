import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
print(abs( max(L) - min(L)))
