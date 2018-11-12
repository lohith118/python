import sys,string, math,itertools

s = input()
n = len(s)
sum1 = 0
for c in s :
    c = c.upper()
    if c.isdigit() :
        sum1 = sum1*16 + (ord(c) - ord('0'))
    elif c >= 'A' and c <= 'F' :
        sum1 = sum1*16 + (ord(c) - ord('A')+10)
print(sum1)







