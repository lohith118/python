import sys,string
def dsum(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1

def isPrime(n) :
    if n==1 : return False
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

n,k = input().split()
n,k = int(n),int(k)
cnt = 0
for i in range(n,k+1) :
    sum1 = dsum(i)
    if isPrime(sum1) :
        cnt += 1
        #print(i,sum1,cnt)
print(cnt)













