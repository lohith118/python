import sys, string, math

# Python3 code for Maximum size square sub-matrix with all 1s

def printMaxSubSquare(M):
    R = len(M)  # no. of rows in M[][]
    C = len(M[0])  # no. of columns in M[][]
    S = [[0 for k in range(C)] for l in range(R)]

    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j - 1], S[i - 1][j],
                              S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0

    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    for i in range(max_i, max_i - max_of_s, -1):
        L = []
        for j in range(max_j, max_j - max_of_s, -1):
            L.append(M[i][j])
        print(*L)

n,k = input().split()
n,k = int(n), int(k)
L = []
for i in range(0,n) :
    L.append({})
for i in range(0,n) :
    L[i] = [ int(x) for x in input().split()]
#print(*L,sep='\n')

printMaxSubSquare(L)