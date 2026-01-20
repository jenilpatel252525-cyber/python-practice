class Solution:
    def maxLength(self, arr):
        masks = []

        # Step 1: convert each string to bitmask
        for s in arr:
            mask = 0
            valid = True
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:     # duplicate in same string
                    valid = False
                    break
                mask |= bit
            if valid:
                masks.append((mask, len(s)))

        self.ans = 0

        # Step 2: DFS over subsets
        def dfs(i, curr_mask, curr_len):
            self.ans = max(self.ans, curr_len)

            for j in range(i, len(masks)):
                next_mask, next_len = masks[j]
                if curr_mask & next_mask == 0:
                    dfs(j + 1, curr_mask | next_mask, curr_len + next_len)

        dfs(0, 0, 0)
        return self.ans
