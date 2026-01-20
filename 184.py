def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n  # Every element is at least an LIS of 1

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)






import bisect

def lengthOfLIS(nums):
    sub = []

    for num in nums:
        i = bisect.bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num

    return len(sub)
