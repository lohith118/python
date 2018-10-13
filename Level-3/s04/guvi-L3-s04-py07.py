import sys,string
def isPalin(s) :
    if s == s[::-1] : return True
    else :            return False

s = input()
L = list(s)
n = len(s)
for i in range(0,n) :
    L2 = L[:]
    L2.pop(i)
    s2 = ''.join(L2)
    if isPalin(s2) :
        print('YES')
        sys.exit()
print('NO')