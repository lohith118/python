import sys,string
s = input()
L = list(s)
#print(L)
n = len(L)
k=1
for i in range(0,n) :
    if L[i].isalpha() :
        if k%2 == 1 :
            L[i] = L[i].upper()
        k += 1
s2 = ''.join(L)
print(s2)









