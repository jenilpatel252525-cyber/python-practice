def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev1 = 0  # max money up to house i - 1
    prev2 = 0  # max money up to house i - 2

    for num in nums:
        temp = prev1
        prev1 = max(prev1, prev2 + num)
        prev2 = temp

    return prev1

nums = [2,3,2]

case1=rob(nums[:-1])

case2=rob(nums[1:])

print(max(case1,case2))