import sys,string, math,itertools

n,a,b = input().split()
n,a,b = int(n),int(a),int(b)
L = [ int(x) for x in input().split()]
ans = max(L)
for x in L :
    if a <= x <= b :
        if x < ans :
            ans = x
print(ans)



