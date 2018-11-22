# no is palindrome
import sys
n = int(input('enter n :'))
s = str(n)
if  s == s[::-1] : print(‘yes’)
else :             print(‘no’)
