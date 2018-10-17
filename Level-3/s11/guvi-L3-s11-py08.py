import sys,string

s = input()
n = len(s)
sum1 = int(s[n-1])
if n == 1 :
    a = int(s[0])
    print(a*a)
    sys.exit()
for i in range(1,n) :
    a = int(s[i-1])
    sum1 += a**(i+1)
    #print(sum1)

print(sum1)










