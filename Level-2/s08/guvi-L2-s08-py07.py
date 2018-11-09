import sys,string, math,itertools

n = int(input())
L = [ int(x) for x in input().split()]
max1 = 0
k = 1
i = 0
while True:
    while L[i] <= L[i+1] :
        k += 1
        i += 1
        if i==n-1 :
            k += 1
            if k > max1:
                max1 = k
            print(max1)
            sys.exit()
    i += 1
    if k > max1 :
        max1 = k
    k = 1
    if i == n-1 :
        print(max1)
        sys.exit()




