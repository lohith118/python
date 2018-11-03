import sys,string, math,itertools

n = int(input())
ans = round(math.sin(n/180 * math.pi),3)
if int(ans) == ans :
    ans = int(ans)
print(ans)