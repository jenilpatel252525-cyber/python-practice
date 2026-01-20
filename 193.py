amount = 5
coins = [1, 2, 5]
coins.sort()

dp = [[0] * (amount + 1) for _ in range(len(coins))]

# Base case: amount 0 can be made in exactly 1 way (choose nothing)
for i in range(len(coins)):
    dp[i][0] = 1

for i in range(len(coins)):
    coin = coins[i]
    for target in range(1, amount + 1):
        # Ways without using this coin
        if i > 0:
            dp[i][target] = dp[i - 1][target]
        # Ways including this coin
        if target >= coin:
            dp[i][target] += dp[i][target - coin]

# Final result
print("Number of ways to make", amount, ":", dp[len(coins) - 1][amount])

# Optional: print DP table
for row in dp:
    print(row)