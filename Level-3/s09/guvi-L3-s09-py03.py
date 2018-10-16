import sys,string
s = input()
for i in range(11,100,11) :
    s2 = str(i)
    if s2 in s :
        i2 = s.index(s2)
        s3 = s[:i2] + s2[0] + s[i2+2:]
        print(s3)
        break


