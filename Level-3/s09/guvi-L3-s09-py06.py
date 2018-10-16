import sys,string
n = int(input())
k = 0
for i in range(1,n+1) :
    s = str(i)
    k += s.count('2')
print(k)




