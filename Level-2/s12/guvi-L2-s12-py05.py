import sys,string, math,itertools

s1,s2 = input().split()
n1,n2 = len(s1), len(s2)
if n1 == n2 :
    print(s1+s2)
elif n1 > n2 :
    s3 = s1[:n2] + s2
    print(s3)
else :
    s3 = s1 + s2[:n1]
    print(s3)









