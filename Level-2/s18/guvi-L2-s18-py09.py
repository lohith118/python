import sys, string, math

n,k = input().split()
n,k = int(n),int(k)
a = n ^ k
s = bin(a)[2:]
ans = s.count('1')
print(ans)


