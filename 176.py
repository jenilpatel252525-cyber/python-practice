def count_zeros_ones(s):
    zeros = s.count('0')
    ones = s.count('1')
    return zeros, ones

def greedy_find_max_form(strs, m, n):
    # Sort by total number of characters (shorter first), or fewer zeros+ones
    strs.sort(key=lambda s: (len(s), s.count('0'), s.count('1')))
    
    count = 0
    for s in strs:
        zeros, ones = count_zeros_ones(s)
        if zeros <= m and ones <= n:
            m -= zeros
            n -= ones
            count += 1
    return count






def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        zeros = s.count('0')
        ones = s.count('1')

        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

    return dp[m][n]