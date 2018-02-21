# dictionary
import sys
d1 = dict(a=1,b=2,c=3)
print(d1)
d1.setdefault('e',5)
print(d1)
d1.setdefault('f',[]).append(6)
print(d1)
d1.setdefault('f',[]).append(7)
print(d1)
c=d1.setdefault('a',0)+1
print(d1,c)
k = 'a'
d1[k] = d1.get('a',0) + 1
k = 'g'
d1[k] = d1.get(k,0) + 1
print(d1)
k = 'a'
d1[k] = d1.setdefault(k,0) + 1
print(d1)
k = 'h'
d1[k] = d1.setdefault(k,0) + 1
print(d1)