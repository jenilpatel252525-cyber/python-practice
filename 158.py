nums = [11,4,3,1,6,5]
total=sum(nums)
        
def canPartition(nums):
    total = sum(nums)
    
    # If total sum is odd, partition is not possible
    if total % 2 != 0:
        return False
    
    nums.sort()

    target=total/2
    
    temp=target

    for i in range(len(nums)-1,-1,-1):
        if nums[i]>target:
            return False
        if nums[i]>temp:
            continue
        temp-=nums[i]
        if temp==0:
            return True
        
    return False
        
print(canPartition(nums))













def canPartition(nums):
    total = sum(nums)
    
    # If total sum is odd, partition is not possible
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    # dp[i] means: is it possible to form sum i using elements from nums
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: 0 sum is always possible with empty set

    for num in nums:
        for j in range(target, num - 1, -1):  # Reverse to avoid reuse
            dp[j] = dp[j] or dp[j - num]

    return dp[target]