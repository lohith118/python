import sys,string
def buildLowestNumber2(str1, n, res) :
    if n == 0 :
        res.append(str1);
        return

    len1 = len(str1);
    if len1 <= n :  return;

    # Find the smallest char among first(n + 1) chars of str.
    minc = min(str1[:n+1])
    min1 = str1.index(minc)
    #print('min1=',minc,min1)
    # Append the smallest char to res -
    res.append(str1[min1]);
    #print(res)

    # substring starting from minIndex +1 to str.length() - 1.
    new_str = str1[min1+1 : ]
    #print('s2=',new_str)

    # Recur for the above substring and n equals to n-minIndex
    buildLowestNumber2(new_str, n-min1, res);

def buildLowestNumber(s1, n) :
    res = []
    buildLowestNumber2(s1, n,res)
    return res

# Driver program
s1,n = input().split()
n = int(n)
L = buildLowestNumber(s1, n)
ans = ''.join(L)
print(ans)
