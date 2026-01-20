from collections import defaultdict

a = [-2, 2, -5, 12, -11, -1, 7]

k = 3
    
s=defaultdict(int)

s[0]=-1

length=0

c=0

for i in range(len(a)):
    c=c+a[i]
    if c % k in s:
        length=max(length,i-s[c%k])
    else:
        s[c%k]=i


print(length)