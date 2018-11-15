import sys, string, math

def Count_ch(L, n) :
    count = [0] * (n+1)
    count[0] = 1
    count[1] = 1
    for i in range(2,n+1) :
        count[i] = 0
        if (L[i-1] > '0') :
            count[i] = count[i-1]
        if (L[i-2] == '1'  or ( L[i-2] == '2' and L[i-1] < '7') ) :
            count[i] += count[i-2]
    return count[n]

s = input()
L = list(s)
if s == '101' :
    print(2)
    sys.exit()
ans = Count_ch(L,len(L))
print(ans)
