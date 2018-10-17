import sys,string
n = int(input())
L = [1]
if n==1 :
    print(*L)
    sys.exit()
print(1)
for i in range(1,n) :
    L = L + [1,1]
    print(*L)












