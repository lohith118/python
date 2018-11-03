import sys,string, math
from itertools import permutations,combinations
def balbr(s) :
    b1=0
    n = len(s)
    if s[0]== '}' :
        return False
    for i in range(0,n) :
        if s[i] == '{' :
            b1 += 1
        if s[i] == '}' :
            b1 -= 1
        if b1<0 :
            return False
    if b1==0 :
        return True
    else :
        return False

n = int(input())
s = '{}'*n
L1 = list(permutations(s))
L2 = [''.join(x) for x in L1]
L3 = []
for x in L2 :
    if balbr(x) :
        L3.append(x)
L4 = []
for x in L3 :
    if x not in L4 :
        L4.append(x)
for x in L4 :
    print(x)







