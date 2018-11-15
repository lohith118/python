import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
dic1 = {}
for x in L :
    dic1[x] = dic1.get(x,0) + 1

min1 = sys.maxsize

for k,v in dic1.items() :
    if v < min1 :
        min1 = v
        key = k
print(key)
