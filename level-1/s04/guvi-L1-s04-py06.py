import sys, string
s = input()
k = 0
for c in s :
    if c.isalnum() or c.isspace(): k += 1
print(len(s)-k)


