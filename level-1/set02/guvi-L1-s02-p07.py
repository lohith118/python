#armstrong no.
n = int(input())
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
   print("yes")
else:
   print("no")

