import sys, string, math
def isPrime(n) :
    if n <= 1 : return False
    if n==2 or n==3 : return True
    a = int(math.sqrt(n)+1)
    for i in range(2,a+1) :
        if n%i == 0 :
            return False
    return True

def factors1(n) :
    L = []
    i = 2
    while n >1 :
        while n%i == 0 :
            L.append(i)
            n //= i
        i += 1
    return L
n,k = input().split()
n,k = int(n), int(k)
if k==0 :
    print(n)
    sys.exit()
a = 10**k
if isPrime(n) :
    print(n * a)
    sys.exit()
L = factors1(n)
#print(L)
cnt2 = L.count(2)
cnt5 = L.count(5)
#print(cnt2,cnt5)
if cnt2 + cnt5 == 0 :
    print(n * a)
    sys.exit()
k = max(k,cnt2,cnt5)
p = 1
for x in L :
    if x != 5 and x != 2 :
        p = p * x
a = p * 10**k
if n >=a :
    print(n)
else :
    print(a)
