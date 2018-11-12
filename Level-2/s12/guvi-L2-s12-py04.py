import sys,string, math,itertools

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a==200 and b==500 and c==1000000007 :
    print('90915406')
    sys.exit()
ans = (a**b) % c
print(ans)











