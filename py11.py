a,b = map(int,input().split())
if a%2==1 : 
	a = a+2
else: 
	a=a+1
for i in range(a,b+1,2) :
	print(i,end=' ')
