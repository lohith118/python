import sys, string, math

def IsIso(string1, string2):
    m = len(string1)
    n = len(string2)
    if m != n:
        return False
    marked = [False] * 256
    map = [-1] * 256
    for i in range(n):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True

# Driver program
s1,s2 = input().split()
if IsIso(s1,s2) : print('yes')
else :            print('no')

