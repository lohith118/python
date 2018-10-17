import sys,string
def isPrime(n) :
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

n = int(input())
flag = 0
for i in range(2,n) :
    for j in range(2,n) :
        if isPrime(i) and isPrime(j) and isPrime(n-i-j) :
            print(i,j,n-i-j)
            flag = 1
            break
    if flag : break











