import sys,string
s = input()
n = len(s)
L = list(s)
L.sort(key = lambda x : L.count(x))
if len(L) - L.count(L[0]) >= L.count(L[0])-1 :
    print('yes')
else :
    print('no')







