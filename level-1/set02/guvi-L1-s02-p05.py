a,b = map(int,input().split())
if a%2==0 :
	a = a+2
else:
	a=a+1
if b%2==0 :
	b = b-2
else:
	b=b-1
for i in range(a,b,2) :
	print(i,end=' ')
print(b)