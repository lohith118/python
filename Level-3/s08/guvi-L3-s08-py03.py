import sys,string

def LCS_2(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    L = []
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    L = []
                    longest = c
                    L.append(S[i-c+1:i+1])
                elif c == longest:
                    L.append(S[i-c+1:i+1])
    res = ''.join(L)
    return res
s1 = input()
s2 = input()
res = LCS_2(s1,s2)
print(res)
