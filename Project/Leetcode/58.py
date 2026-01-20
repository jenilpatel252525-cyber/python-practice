from collections import defaultdict

a = [5,6,7,8,9]

k=5

s=defaultdict(int)

count=0

s[0]=1

x=0

for i in a:
    x = x ^ i
    for j in s:
        if x ^ j < k:
            count += s[j]
    s[x]+=1


print(count)