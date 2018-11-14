import sys,string, math,itertools

def isPrime(n) :
    if n==1 : return False
    if n==2 or n==3 : return True
    for i in range(2,n) :
        if n%i==0 :
            return False
    return True

s = input()
n = len(s)
if isPrime(n) :
    print('yes')
else :
    print('no')