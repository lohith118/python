import sys,string, itertools


# A Recursive  program to solve minimum sum partition problem.

# Function to find the minimum sum
def findMin2(L, i, sumCalculated, sumTotal) :
    if i == 0:
        return abs((sumTotal - sumCalculated) - sumCalculated)

    return min(findMin2(L, i-1, sumCalculated + L[i-1], sumTotal),
               findMin2(L, i-1, sumCalculated, sumTotal))


def findMin(L, n):
    sumTotal = 0;
    for i in range(0, n):
        sumTotal += L[i];
    return findMin2(L, n, 0, sumTotal)

n = int(input())
L = [ int(x) for x in input().split()]
print(findMin(L, n))
