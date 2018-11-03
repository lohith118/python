import sys,string, math,itertools

s = input()
L = s.split()
n = len(s)
#print(s,L)
L2 = []
for s2 in L :
    for j in range(0,len(s2)) :
        if s.count(s2[j]) == 1 :
            L2.append(s2[j])
print(*L2)

