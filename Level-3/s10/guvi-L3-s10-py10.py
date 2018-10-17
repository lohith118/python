import sys,string
def isPrime(n) :
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

n = int(input())
for i in range(2,n) :
    if isPrime(i) and isPrime(n-i):
        print(i, n-i)
        break











