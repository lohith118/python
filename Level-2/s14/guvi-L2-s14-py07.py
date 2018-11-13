import sys,string, math,itertools

n = int(input())
s = bin(n)[2:]
s2 = s[::-1]
ans = s2.index('1') + 1
print(ans)



