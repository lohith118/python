import sys,string, math,itertools

s = input()
n = len(s)
a = int(s[0])
if a%2 == 1 :
    prev = 'Odd'
else :
    prev = 'Even'
max1 = 0
k = 1
for i in range(1,n) :
    #print('i=',i,s[i])
    a = int(s[i])
    if a%2==1 :
        #print('1.',prev,k)
        if prev == 'Even' :
            k += 1
            prev = 'Odd'
            if k > max1 :
                max1 = k
        else :
            k = 1
        #print(prev, k,max1)
    else :
        #print('2.',prev,k)
        if prev == 'Odd' :
            k += 1
            prev = 'Even'
            if k > max1 :
                max1 = k
        else :
            k = 1
        #print(prev, k,max1)
print(max1)




