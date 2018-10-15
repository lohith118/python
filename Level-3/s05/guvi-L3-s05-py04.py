import sys,string, itertools
n = int(input())
k2 = 0
for i in range(1,34) :
    for j in range(0,2**i) :
        k2 += 1
        if k2 == n :
            s3 = bin(j)[2:]
            k = i - len(s3)
            s32 = '0'*k + s3
            s4 = s32.replace('0', '3')
            s4 = s4.replace('1', '4')
            print(s4)
            sys.exit()
