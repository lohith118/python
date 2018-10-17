import sys,string

def isPrime(n) :
    if n==1 : return False
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

n = int(input())
cnt = 0
for i in range(2,n//2+1) :
    if isPrime(i) and isPrime(n-i)  :
        cnt += 1
        #print(i,n-i,cnt)
print(cnt)













