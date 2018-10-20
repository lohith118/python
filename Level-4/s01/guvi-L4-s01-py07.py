import sys, string, math
n = int(input())
k = len(bin(n)[2:])
print(n-2**(k-1))



