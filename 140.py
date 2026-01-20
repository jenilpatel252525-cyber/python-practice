def stock(prices):
    n = len(prices)
    ans = [0]  # use list to simulate nonlocal mutable
    total = [0]

    def dfs(i, curr):
        if i >= n:
            ans[0] = max(ans[0], total[0])
            return
        if curr is None:
            # Option 1: Buy at i
            dfs(i + 1, prices[i])
            # Option 2: Skip
            dfs(i + 1, None)
        else:
            for j in range(i, n):
                profit = prices[j] - curr
                if profit < 0:
                    continue
                total[0] += profit
                dfs(j + 2, None)  # cooldown
                total[0] -= profit

    dfs(0, None)
    return ans[0]


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, n):
            prev_hold = hold
            hold = max(hold, rest - prices[i])
            rest = max(rest, sold)
            sold = prev_hold + prices[i]

        return max(sold, rest)