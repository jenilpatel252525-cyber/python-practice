a=[2,3,2,1,2,4,3,7]

target=7

curr=0

length=float("inf")

i=0
j=0

while j<len(a):
    curr+=a[j]
    if curr > target:
        while curr>target:
            curr-=a[i]
            i+=1
    if curr==target:
        length=min(length,j-i+1)
        print(length)
        curr-=a[i]
        i+=1
    j+=1
    
print(length)









def minSubArrayLen(target, nums):
    n = len(nums)

    # Step 1: Build prefix sum array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    def binary_search(left, right, value):
        # Find the smallest index j such that prefix[j] >= value
        while left < right:
            mid = (left + right) // 2
            if prefix[mid] < value:
                left = mid + 1
            else:
                right = mid
        return left

    min_len = float('inf')

    # Step 2: For each i, binary search for the smallest j where prefix[j] - prefix[i] >= target
    for i in range(n):
        required = target + prefix[i]
        bound = binary_search(i + 1, n + 1, required)
        if bound <= n:
            min_len = min(min_len, bound - i)

    return 0 if min_len == float('inf') else min_len
