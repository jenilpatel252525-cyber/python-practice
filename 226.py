from collections import Counter
from functools import lru_cache

def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k

    freq = Counter(nums)
    nums = sorted(freq.keys(), reverse=True)  # big first for pruning

    @lru_cache(None)
    def dfs(cur_target, used_tuple, groups):
        if groups == k:  # formed k groups successfully
            return True
        if cur_target == 0:
            # one subset filled, start new subset
            return dfs(target, used_tuple, groups+1)

        used = dict(zip(nums, used_tuple))
        for num in nums:
            if used[num] > 0 and num <= cur_target:
                used[num] -= 1
                new_tuple = tuple(used[n] for n in nums)
                if dfs(cur_target - num, new_tuple, groups):
                    return True
                used[num] += 1
        return False

    return dfs(target, tuple(freq[n] for n in nums), 0)



