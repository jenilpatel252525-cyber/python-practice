a=[1, 3, 6, 24, 36, 72, 2, 4, 12, 18, 9, 8, 16]

def largestDivisibleSubsetLength(nums):
    if not nums:
        return 0

    nums.sort()
    n = len(nums)
    dp = [1] * n  # dp[i] = length of largest divisible subset ending at nums[i]

    max_len = 1

    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])

    return max_len