def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    dp = [False] * (target + 1)
    dp[0] = True  # Base case: 0 sum is always possible

    for num in nums:
        for i in range(target, num - 1, -1):  # Traverse backwards
            dp[i] = dp[i] or dp[i - num]

    return dp[target]
