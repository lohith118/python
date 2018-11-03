import sys,string, math

s = input()
if s.count('@') ==0 or s.count('@') > 1 :
    print('NO')
    sys.exit()
if '&' in s and  s.count('&') > 1 :
    print('NO')
    sys.exit()
if s[-4:] != '.com' :
    print('NO')
    sys.exit()
i1 = s.index('@')
i2 = s.index('.com')
if (i2 - i1) < 5 :
    print('NO')
    sys.exit()
if i1 < 3 :
    print('NO')
    sys.exit()
print('YES')









