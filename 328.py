class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])

        # sorted[i] = True means strs[i] < strs[i+1] is already decided
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            # Step 1: check if this column causes a violation
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue  # delete this column

            # Step 2: use this column to fix ordering
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

            # Optimization: if all pairs sorted, we can stop early
            if all(sorted_pairs):
                break

        return deletions
