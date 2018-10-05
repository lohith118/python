#armstrong no.
L = []
a,b = map(int,input().split())
a = a+1
for n in range(a,b) :
    nd = 0
    m = n
    while m>0 :
	    nd += 1
	    m //= 10
    sum = 0
    temp = n
    while temp > 0:
        d = temp % 10
        sum += d ** nd
        temp //= 10
    if n == sum:
        L.append(n)
print(*L)


