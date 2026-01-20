from collections import defaultdict

from operator import xor

a = [1, 2, 3, 4, 5, 6, 7, 8]

k=4

s=defaultdict(int)

count=0

x=0

s[0]=1

for i in range(len(a)):
    x=x ^ a[i]
    if x % k in s:
        count+=s[x % k]
    s[x]+=1

print(count)



