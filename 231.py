def maxProfit(prices, fee):
    hold = -prices[0]   # profit if holding stock after day 0
    cash = 0            # profit if not holding stock after day 0
    
    for price in prices[1:]:
        hold = max(hold, cash - price)         # buy or hold
        cash = max(cash, hold + price - fee)   # sell or stay out
    
    return cash


prices = [1,3,2,8,4,9]
fee = 2





def maxProfit_2D_optimized(prices, fee):
    n = len(prices)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n):  # interval length
        for i in range(n - length):
            j = i + length

            # option 1: don't sell at j
            profit1 = dp[i][j-1]

            # option 2: direct buy at i, sell at j
            profit2 = max(0, prices[j] - prices[i] - fee)

            # option 3: split at (j-1)
            profit3 = dp[i][j-2] + dp[j-1][j] if j-1 > i else 0

            dp[i][j] = max(profit1, profit2, profit3)

    return dp[0][n-1]
