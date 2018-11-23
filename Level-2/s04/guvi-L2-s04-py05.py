import sys,string, math,itertools

import sys, string
def minChCnt(s) :
    dic1 = {}
    for c in s :
        if not c.isspace() :
            dic1[c] = dic1.get(c,0) + 1
    min1 = sys.maxsize
    L = []
    for x in dic1.values() :
        if x < min1 :
            min1 = x
    for k,v in dic1.items() :
        if v == min1 :
            L.append(k)
    return L

s = input()
n = len(s)
L = minChCnt(s)
L3 = [x.lower() for x in L]
print(*L3)

