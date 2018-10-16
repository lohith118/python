import sys,string
#Python prog to find the smallest number which > the given no.
# has same set of digits as given number

def findNext(L, n):
    # Start from the right most digit and find the first
    # digit that is smaller than the digit next to it
    for i in range(n - 1, 0, -1):
        if ord(L[i]) > ord(L[i-1]):
            break
    # If no such digit found,then all numbers are in
    # descending order, no greater number is possible
    if i == 0:
        return "impossible"

    # Find the smallest digit on the right side of
    # (i-1)'th digit that is greater than number[i-1]
    x = ord(L[i-1])
    smallest = i
    for j in range(i + 1, n):
        if ord(L[j]) > x and ord(L[j]) < ord(L[smallest]) :
            smallest = j
            # Swapping the above found smallest digit with (i-1)'th
    L[smallest], L[i-1] = L[i-1], L[smallest]

    L2 = L[:i]
    L3 = sorted(L[i:])
    L4 = L2 + L3
    res = ''.join(L4)
    #print(L4)
    return res

# Driver Program to test above function
s = input()

L = list(s)
res = findNext(L, len(L))
print(res)








