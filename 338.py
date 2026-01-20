from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs():
            res = 0
            for ch in count:
                if count[ch] > 0:
                    # choose
                    count[ch] -= 1
                    res += 1          # current sequence is valid
                    res += dfs()      # extend sequence
                    count[ch] += 1    # backtrack
            return res

        return dfs()