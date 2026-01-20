from collections import Counter

def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        count = Counter(s)
        zeros, ones = count['0'], count['1']

        # Iterate backwards to avoid overwriting results of current iteration
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

    return dp[m][n]