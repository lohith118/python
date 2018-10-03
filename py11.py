a,b = map(int,input().split())
print(a,b)
if a % 2 == 0 : a = a+1
for i in range(a,b+1,2) :
	print(i,sep=' ')
