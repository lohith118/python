import sys,string, math,itertools

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a==0 or b==0 or c==0 :
    print('no')
    sys.exit()
if a+b+c == 180:
    print('yes')
else :
    print('no')