import sys,string
def isPalin(s) :
    if s == s[::-1] : return True
    else :            return False

n = int(input())
m = n
sum1 = 0
while m :
    sum1 += m%10
    m //= 10
s = str(sum1)
#print(s)
if isPalin(s) :
    print('YES')
else :
    print('NO')