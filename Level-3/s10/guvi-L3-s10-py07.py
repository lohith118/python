import sys,string
def hcf(a,b) :
    min1 = min(a,b)
    for i in range(1,min1+1) :
        if a%i == 0  and  b%i == 0 :
            hcf1 = i
    return hcf1
n,k = input().split()
n,k = int(n),int(k)
k = hcf(n,k)
if k==1 : print('yes')
else :    print('no')











