# a=[1,2,3,0,2,0,1]
# k=3
# sum=0
# c=0
# j=0

# for i in range(len(a)):
#     sum+=a[i]
#     while sum>k:
#         sum-=a[j]
#         j+=1
#     if a[j]==0 and sum==k:
#         c+=2
#     elif sum==k:
#         c+=1

# print(c)

from collections import defaultdict

a = [1, 2, 3, 0, 2, 0, 1]
k = 3
prefix_sum = 0
count = 0
sum_freq = defaultdict(int)
sum_freq[0] = 1  # Base case: subarray that starts at index 0

for num in a:
    prefix_sum += num
    if (prefix_sum - k) in sum_freq:
        count += sum_freq[prefix_sum - k]
    sum_freq[prefix_sum] += 1

print(count)
