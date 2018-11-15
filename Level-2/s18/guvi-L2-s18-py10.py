import sys, string, math

s = input()
if s.count('1') == 1 :
    ans = int(s,2)
else :
    k = len(s)
    ans = 2**k
print(ans)

