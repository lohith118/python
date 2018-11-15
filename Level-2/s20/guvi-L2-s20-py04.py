import sys, string, math

s1,s2 = input().split()
if s1 == 'P' and s2 == 'R' or s1 == 'R' and s2 == 'P' :
    print('P')
elif s1 == 'P' and s2 == 'S' or s1 == 'S' and s2 == 'P' :
    print('S')
elif s1 == 'S' and s2 == 'R' or s1 == 'R' and s2 == 'S' :
    print('R')
elif s1 == 'S' and s2 == 'S' :
    print('D')
elif s1 == 'P' and s2 == 'P' :
    print('D')
elif s1 == 'R' and s2 == 'R' :
    print('D')
