def canPartition(nums,target):
    total = sum(nums)

    target = (total+target) // 2
    
    if target % 2 != 0:
        return
    
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: 0 sum is always possible

    for num in nums:
        for i in range(target, num - 1, -1):  # Traverse
            dp[i] = dp[i] + dp[i - num]

    print(dp)

canPartition([1,1,1,1,1],3)