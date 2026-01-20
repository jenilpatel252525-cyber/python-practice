# a=[1, 1, 0, 1, 0, 1, 1]
# length=0
# count0=0
# count1=0
# i=0
# j=1
# sum=0

# for k in range(len(a)):
#     if a[k]==0:
#         a[k]=-1

# while i<len(a):
#     sum=sum+a[i]
#     while j<len(a):
#         sum=sum+a[j]
#         if sum==0:
#             length=max(length,j-i+1)
#         j+=1
#     i+=1
#     j=i+1
#     sum=0

# print(length)


a = [1, 1, 0, 1, 0, 1, 1]

# Step 1: Convert 0s to -1s
for i in range(len(a)):
    if a[i] == 0:
        a[i] = -1

# Step 2: Find the longest subarray with sum = 0
prefix_sum = 0
max_len = 0
sum_index_map = {}  # Maps prefix_sum to its first occurrence index

for i in range(len(a)):
    prefix_sum += a[i]

    if prefix_sum == 0:
        max_len = i + 1

    if prefix_sum in sum_index_map:
        max_len = max(max_len, i - sum_index_map[prefix_sum])
    else:
        sum_index_map[prefix_sum] = i

print(max_len)
