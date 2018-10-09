import sys, string, math
s = input()
vow = 'aeiou'
s2 = ''
for c in s :
    if c not in vow : s2 = s2 + c
print(s2[::-1])
