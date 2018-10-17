import sys,string
def isPrime(n) :
    for i in range(2,n) :
        if n%i == 0 :
            return False
    else :
        return True

n = int(input())

L = []
for i in range(2,n) :
    if isPrime(i) :
        L.append(i)

print(*L)










