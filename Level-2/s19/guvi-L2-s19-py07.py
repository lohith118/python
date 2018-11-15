import sys, string, math

s1,s2 = input().split()
n1,n2 = len(s1), len(s2)
if n1%n2 == 0 or n2%n1 == 0 :
    print('no')
else :
    print('yes')

