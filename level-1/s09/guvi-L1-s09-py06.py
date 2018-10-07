import sys, string, math
s = input()
L = list(set(s))
k = s.count(L[0])
for i in range(1,len(L)) :
    if s.count(L[i]) != k :
        print('No')
        sys.exit()
print('Yes')
