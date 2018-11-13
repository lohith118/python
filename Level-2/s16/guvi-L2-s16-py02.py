import sys,string, math,itertools

s = input()
vow = 'aeiou'
k = 1
max1 = 0
if s[0] in vow :
    prev = 'V'
else :
    prev = 'C'
for i in range(1,len(s)) :
    c = s[i]
    if c in vow :
        if prev=='C' :
            prev = 'V'
            k += 1
            if k > max1 :
                max1 = k

        else :
            k = 1
    else :
        if prev == 'V':
            prev = 'C'
            k += 1
            if k > max1:
                max1 = k
        else:
            k = 1
print(max1)