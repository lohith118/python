import sys,string
s = input()
L = list(s)
n = len(s)
k = n//2
for i in range(0,n) :
    L2 = L[:]
    L2.pop(i)
    s2 = ''.join(L2)
    #print(s2)
    if s2[:k] == s2[k:] :
        print('YES')
        sys.exit()
print('NO')