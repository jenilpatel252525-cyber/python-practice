from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        # Step 1: build universal requirement from words2
        required = Counter()

        for w in words2:
            freq = Counter(w)
            for ch in freq:
                required[ch] = max(required[ch], freq[ch])

        # Step 2: check each word in words1
        res = []
        for w in words1:
            freq = Counter(w)
            ok = True
            for ch in required:
                if freq[ch] < required[ch]:
                    ok = False
                    break
            if ok:
                res.append(w)

        return res
