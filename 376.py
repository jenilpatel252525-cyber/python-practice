s = "aacaba"

from collections import defaultdict

class Solution:
    def numSplits(self, s: str) -> int:
        left = defaultdict(int)
        right = defaultdict(int)

        # fill right frequency map
        for ch in s:
            right[ch] += 1

        left_unique = 0
        right_unique = len(right)
        ans = 0

        # iterate till second last char
        for ch in s[:-1]:
            # move char from right to left
            left[ch] += 1
            if left[ch] == 1:
                left_unique += 1

            right[ch] -= 1
            if right[ch] == 0:
                right_unique -= 1

            if left_unique == right_unique:
                ans += 1

        return ans










class Solution:
    def numSplits(self, s: str) -> int:
        left = [0] * 26
        right = [0] * 26

        for ch in s:
            right[ord(ch) - 97] += 1

        left_unique = 0
        right_unique = sum(1 for x in right if x > 0)

        ans = 0

        for ch in s[:-1]:
            idx = ord(ch) - 97

            if left[idx] == 0:
                left_unique += 1
            left[idx] += 1

            right[idx] -= 1
            if right[idx] == 0:
                right_unique -= 1

            if left_unique == right_unique:
                ans += 1

        return ans
