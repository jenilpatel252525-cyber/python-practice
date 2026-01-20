a = [4,6,7,7]
n = len(a)

dp = [1] * n
prev = [-1] * n  # To store the index of previous element in the subsequence

# Fill dp and prev arrays
for i in range(1, n):
    for j in range(i):
        if a[i] >= a[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

# Find the index of the last element of the longest subsequence
max_len = max(dp)
idx = dp.index(max_len)

# Reconstruct the sequence using the prev array
sequence = []
while idx != -1:
    sequence.append(a[idx])
    idx = prev[idx]

sequence.reverse()  # Since we built it backwards

from typing import List

def findSubsequences(nums: List[int]) -> List[List[int]]:
    res = set()
    n = len(nums)

    def dfs(start, path):
        if len(path) >= 2:
            res.add(tuple(path))  # Use tuple to store in set to avoid duplicates
        for i in range(start, n):
            if not path or nums[i] >= path[-1]:
                dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return [list(seq) for seq in res]

# Example usage
nums = [1, 2, 3, 3, 4, 5, 6]
result = findSubsequences(nums)
print("Total:", len(result))
for seq in sorted(result):
    print(seq)











def findSubsequences(nums):
    result = set()

    def backtrack(start, path):
        if len(path) >= 2:
            result.add(tuple(path))  # Tuples are hashable and can go into set

        used = set()  # To prevent duplicates at the same level
        for i in range(start, len(nums)):
            if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                used.add(nums[i])
                backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return [list(seq) for seq in result]
