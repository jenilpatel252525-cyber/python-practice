s = "heeellooo", words = ["hello", "hi", "helo"]

class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:

        def isExpressive(word):
            i = j = 0
            n, m = len(s), len(word)

            while i < n and j < m:
                if s[i] != word[j]:
                    return False

                # count group length in s
                i0 = i
                while i < n and s[i] == s[i0]:
                    i += 1
                lenS = i - i0

                # count group length in word
                j0 = j
                while j < m and word[j] == word[j0]:
                    j += 1
                lenW = j - j0

                # apply rules
                if lenS < lenW:
                    return False
                if lenS != lenW and lenS < 3:
                    return False

            # both strings must be fully consumed
            return i == n and j == m

        count = 0
        for w in words:
            if isExpressive(w):
                count += 1

        return count
