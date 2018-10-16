import sys,string
s = input()
n = len(s)
s2 = ''
m = n
i=0
while m > 0:
    k=0
    c = s[i]
    while i<n and s[i] == c :
        k += 1
        i += 1
    if k>1 :
        s2 = s2 + str(k) + '*' + c
        m -= k
    else :
        s2 = s2 + c
        m -= 1
print(s2)




