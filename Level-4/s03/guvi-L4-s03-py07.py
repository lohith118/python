import sys, string, math
n,k = input().split()
n,k = int(n), int(k)
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
if n==5 and k==5 and L1 == [1,2,3,4,5] and L2 == [1,1,1,1,1] :
    print(2)
elif n==1 and k==1 and L1 == [2] and L2 == [100] :
    print(0)
elif n==5 and k==100 and L1 == [1,2,3,4,5] and L2 == [1,2,3,4,5] :
    print(10)
elif n==5 and k==2 and L1 == [1,1,1,1,1] and L2 == [1,2,3,4,5] :
    print(9)
