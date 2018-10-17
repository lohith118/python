import sys,string

s = input()
print(s)
n = len(s)
sum1 = 0
for i in range(0,n) :
    sum1 += int(s[i])**i
print(sum1)












