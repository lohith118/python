import sys,string
a,b,n = input().split()
a,b,n = int(a),int(b),int(n)
sn = str(n)
cnt = 0
for i in range ( a, b+1) :
    s = str(i)
    if sn in s :
        cnt += 1
print(cnt)










