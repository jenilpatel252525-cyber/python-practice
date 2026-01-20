from collections import defaultdict

a=[1,2,3]

k=3

s=defaultdict(int)

s[0]=1

sum1=0

count=0

for i in range(len(a)):
    sum1=sum1 + a[i]
    if sum1-k in s:
        count+=s[sum1-k]
    s[sum1]+=1

print(count)