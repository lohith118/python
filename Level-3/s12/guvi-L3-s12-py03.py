import sys,string, math

n = int(input())
s2 = bin(n)[2:]
if s2.count('1') == 1 :
    print('YES')
else :
    print('NO')