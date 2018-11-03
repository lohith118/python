import sys,string, math,itertools

s = input()
b1=0
n = len(s)
if s[0]== ')' :
    printf("no")
    sys.exit()
for i in range(0,n) :
    if s[i] == '(' :
        b1 += 1
    if s[i] == ')' :
        b1 -= 1
    if b1<0 :
        printf("no")
        sys.exit()
if b1==0 :
    print("yes")
else :
    print("no")


