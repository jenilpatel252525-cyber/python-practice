words = ["a","b","ba","bca","bda","bdca"]

class Solution:
    def longestStrChain(self, words):
        # Step 1: sort by length
        words.sort(key=len)

        dp = {}  # dp[word] = longest chain ending at word
        ans = 1

        for word in words:
            best = 1  # chain of at least length 1 (the word itself)

            # Step 2: try removing one character
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]

                if prev in dp:
                    best = max(best, dp[prev] + 1)

            dp[word] = best
            ans = max(ans, best)

        return ans
