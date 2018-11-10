import sys,string, math,itertools

s = input()
for c in s :
    if s.count(c) > 1 :
        print('yes')
        sys.exit()
print('no')








