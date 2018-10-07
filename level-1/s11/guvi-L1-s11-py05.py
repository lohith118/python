import sys, string, math
a,b = map(int,input().split())
k = len(str(b))
ans = a * 10**k + b
print(ans)