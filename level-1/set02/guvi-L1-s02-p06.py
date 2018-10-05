a,b = map(int,input().split())
a = a+1
L = []
for i in range(a,b) :
	for j in range(2,i) :
		if i%j == 0 :
			break
	else :
		L.append(i)
print(*L)

