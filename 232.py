def findLength(nums1, nums2):
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    max_len = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0

    return max_len








def findLength(nums1, nums2):
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)
    prev = [0]*(m+1)
    max_len = 0

    for i in range(1, n+1):
        curr = [0]*(m+1)
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                curr[j] = prev[j-1] + 1
                max_len = max(max_len, curr[j])
        prev = curr

    return max_len