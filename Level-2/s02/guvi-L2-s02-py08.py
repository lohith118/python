import sys, string, math
def freq1(s) :
    dic1 = {}
    for c in s :
        if c in dic1 :
            dic1[c] += 1
        else :
            dic1[c] = 1
    return dic1

k = 0
s1 = 'kabali'
dic1 = freq1(s1)
n = int(input())
for i in range(n) :
    s2 = input()
    dic2 = freq1(s2)
    if dic1 == dic2 : k += 1
print(k)


