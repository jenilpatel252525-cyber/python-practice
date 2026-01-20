# from collections import defaultdict

# a= [2,3,1,2,4,3]

# target = 7  

# length=0

# s=defaultdict(int)

# c=0

# j=0

# for i in range(len(a)):
#     c+=a[i]
#     if c>=target:
#         if length==0:
#             length=i-j+1
#         else:
#             length=min(length,i-j+1)
#         while c-a[j]>=target and j<len(a)-1:
#             c-=a[j]
#             j+=1
#             if c-a[j]>=target:
#                 length=min(length,i-j+1)

# print(length)

a = [2, 3, 1, 2, 4, 3]
target = 7

c = 0
j = 0
length = float('inf')

for i in range(len(a)):
    c += a[i]
    while c >= target:
        length = min(length, i - j + 1)
        c -= a[j]
        j += 1

print(length if length != float('inf') else 0)
