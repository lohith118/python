import sys, string, math
a,d,n = map(int,input().split())
tn = a + (n-1)*d
sum1 =n*(a+tn)//2
print(sum1)

