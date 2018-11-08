import sys,string, math,itertools

n = int(input())
L1 = [ int(x) for x in input().split()]
L3 = [x for x in L1 if x < n]


print(*L3)