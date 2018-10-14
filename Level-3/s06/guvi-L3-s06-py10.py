import sys, string, math
n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
L3 = []
k = 0
if L1 == L2 :
    print(0)
    sys.exit()
for i in range(1,n) :
    L3 = L1[i:] + L1[:i]
    if L3 == L2 :
        print(i)
        break
