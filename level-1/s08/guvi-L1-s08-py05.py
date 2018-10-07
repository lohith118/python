import sys, string
s = input()
k = len(s)
m = k//2
if k%2 == 1 : s2 = s[:m] + '*' + s[m+1:]
else :        s2 = s[:m-1] + '**' + s[m+1:]
print(s2)
