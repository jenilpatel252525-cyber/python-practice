s = "abcd"
t = "bcdf"
maxCost = 3

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        currCost = 0
        ans = 0

        for r in range(len(s)):
            currCost += abs(ord(s[r]) - ord(t[r]))

            while currCost > maxCost:
                currCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            ans = max(ans, r - l + 1)

        return ans
