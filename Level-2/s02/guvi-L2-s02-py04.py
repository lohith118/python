import sys, string, math
n = int(input())
s = input()
vow = 'aeiouAEIOU'
s2 = ''
for c in s :
    if c not in vow : s2 = s2 + c
print(s2[::-1])
