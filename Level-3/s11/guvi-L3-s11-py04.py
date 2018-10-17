import sys,string
def dgtSum(n) :
    sum1 = 0
    while(n) :
        sum1 += n%10
        n //= 10
    return sum1
s = input()
sum1 = 0
n = len(s)
for i in range(1,n+1) :
    s2 = s[:i]
    #print(s2)
    sum1 += dgtSum(int(s2))
print(sum1)










