words = ["a","banana","app","appl","ap","apply","apple"]

words.sort()

class Solution:
    def longestWord(self, words):
        # Sort lexicographically so ties are handled (lexicographically smaller seen first)
        words.sort()
        valid = set([""])      # base: empty prefix allowed
        best = ""

        for w in words:
            if w[:-1] in valid:     # all prefixes exist by induction
                valid.add(w)
                # update best: longer wins; if equal length, lexicographically smaller
                if len(w) > len(best):
                    best = w

        return best
