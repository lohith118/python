import sys, string, math
from itertools import permutations, combinations
n = int(input())
k = 2**n
for i in range(0,k) :
    s = bin(i)[2:]
    j = len(s)
    if j < n :
        s = '0' * (n-j) + s
    print(s)







