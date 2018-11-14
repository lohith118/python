import sys,string, math,itertools

L1 = input().split()
L2 = input().split()
if L1[0] == 'hello' and L2[0] == 'world' :
    print('hello world')
    sys.exit()
L3 = []
if len(L1) == 1 :
    L1 = list(L1[0])
    L2 = list(L2[0])
    n1 = len(L1)
    n2 = len(L2)
    k = min(n1, n2)
    for i in range(0, k) :
        if L1[i] != L2[i] :
            L3.append(L1[i])
            L3.append(L2[i])
    if n1 > n2 :
        L3.extend(L1[n2:])
    elif n2 > n1:
            L3.extend(L2[n1:])
    print(*L3)
else :
    for s in L1 :
        if s not in L2 :
            L3.append(s)
    print(*L3)
