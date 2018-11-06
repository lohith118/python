import sys, string, math
s1,s2 = input().split()
n = len(s1)
for c in s1 :
    if c in s2 :
        print('yes')
        sys.exit()
print('no')