from operator import xor

a=[2, 3, 1, 6, 7]

k=3

x=0

count=0

s={}

for i in range(len(a)):
    if a[i]==k:
        count+=1
    x=xor(x,a[i])
    if x==k:
        count+=1
    s[i]=x

j=0
x2=0
flag=False

while j<len(s):
    if s[j]==k:
        flag=True
    if flag:
        x2=xor(x2,s[j])
        if x2==0:
            count+=1
            flag=False
    j+=1

print(s)
print(count)

# from collections import defaultdict
# from operator import xor

# a = [5, 6, 7, 8, 9]
# k = 5

# count = 0
# x = 0
# freq = defaultdict(int)
# freq[0] = 1  # to handle case when prefix xor itself is equal to k

# for num in a:
#     x = xor(x, num)
#     count += freq[x ^ k]
#     freq[x] += 1

# print(count)

[1], [2], [1,2], [3], [1,2,3], [2,3]