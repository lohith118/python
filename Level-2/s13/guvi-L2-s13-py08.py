import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
ans = 'odd'
for x in L :
    if x%2 == 0 :
        ans = 'even'
        break
print(ans)





