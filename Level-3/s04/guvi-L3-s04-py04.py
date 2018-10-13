import sys,string
from itertools import permutations

s = input()
L = list(permutations(s))
L2 = [ ''.join(x) for x in L]
L3 = list(set(L2))
#print(L3)
L4 = [ int(x) for x in L3]
if len(L4) == 1 :
    print('impossible')
    sys.exit()
n = int(s)
#print(L4)
max1 = max(L4)
if max1 <= n :
    print('impossible')
    sys.exit()
for i in range(0,len(L4)) :
    if L4[i] > n :
        if L4[i] < max1 :
            max1 = L4[i]
print(max1)

