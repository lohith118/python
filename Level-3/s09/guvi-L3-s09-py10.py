import sys,string
s = input()
n = len(s)
i=0
max1 = 0
while i<n:
    k=0
    c = s[i]
    while i<n and s[i] == c :
        k += 1
        i += 1
    if k > max1 :
        max1 = k
        c2 = c
print(c2,max1)



