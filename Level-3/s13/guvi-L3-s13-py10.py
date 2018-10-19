import sys, string, math
def isPrime(n) :
	if n==1 : return  False
	if n==2 or n==3 : return True
	for i in range(2,n) :
		if n%i == 0 :
			return False
	return True

n = int(input())
sum1 = 0
for i in range(3,n+1) :
	if isPrime(i) :
		#print(i)
		if i%3 == 0 :
			sum1 += i
print(sum1)


