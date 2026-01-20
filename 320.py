s = "(()(()))()(())"

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dp = {}
        stack = []

        # Step 1: build matching map
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                dp[stack.pop()] = i

        # Step 2: recursive scoring
        def dfs(l, r):
            score = 0
            i = l
            while i <= r:
                j = dp[i]
                if j == i + 1:     # "()"
                    score += 1
                else:              # "(A)"
                    score += 2 * dfs(i + 1, j - 1)
                i = j + 1          # move to next segment
            return score

        return dfs(0, len(s) - 1)





        
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth   # 2^depth

        return score






class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack[0]
