class Solution:
    def numSpecialEquivGroups(self, words):
        groups = set()

        for w in words:
            even = [0] * 26
            odd = [0] * 26

            for i, ch in enumerate(w):
                idx = ord(ch) - ord('a')
                if i % 2 == 0:
                    even[idx] += 1
                else:
                    odd[idx] += 1

            groups.add((tuple(even), tuple(odd)))

        return len(groups)

from collections import Counter

class Solution:
    def numSpecialEquivGroups(self, words):
        groups = set()

        for w in words:
            even_counter = Counter()
            odd_counter = Counter()

            for i, ch in enumerate(w):
                if i % 2 == 0:
                    even_counter[ch] += 1
                else:
                    odd_counter[ch] += 1

            # convert to immutable form so it can be stored in a set
            groups.add((
                tuple(sorted(even_counter.items())),
                tuple(sorted(odd_counter.items()))
            ))

        return len(groups)


class Solution:
    def numSpecialEquivGroups(self, words):
        seen = set()

        for w in words:
            even = sorted(w[0::2])   # chars at even indices
            odd = sorted(w[1::2])    # chars at odd indices
            seen.add((tuple(even), tuple(odd)))

        return len(seen)
