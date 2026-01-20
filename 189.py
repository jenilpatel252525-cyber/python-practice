def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    # Create a DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Need i deletions to convert word1[0...i-1] to ""
    for j in range(n + 1):
        dp[0][j] = j  # Need j insertions to convert "" to word2[0...j-1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No change needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Delete from word1
                                   dp[i][j - 1],    # Insert into word1
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

# Example
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # Output: 3