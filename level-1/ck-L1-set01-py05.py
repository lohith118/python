#largest of 3 nos
import sys
a,b,c = map(int,(input('enter 3 nos : ').split()))
#print(a,b,c)
if a>b and a>c : print(a)
elif b>c : print(b)
else : print(c)

