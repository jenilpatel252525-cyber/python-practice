from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)
        count = defaultdict(int)

        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # maintain window size = minSize
            if right - left + 1 > minSize:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            # check validity
            if right - left + 1 == minSize and len(count) <= maxLetters:
                freq[s[left:right+1]] += 1

        return max(freq.values(), default=0)
