def longestPalindromeSubseq(s: str) -> int:
    t = s[::-1]
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][n]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1

        # Check substrings of increasing length
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]
