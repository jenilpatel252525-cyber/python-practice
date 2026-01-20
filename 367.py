class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)
        active = 0
        max_frogs = 0

        for ch in croakOfFrogs:
            cnt[ch] += 1

            if not (cnt['c'] >= cnt['r'] >= cnt['o'] >= cnt['a'] >= cnt['k']):
                return -1

            if ch == 'c':
                active += 1
                max_frogs = max(max_frogs, active)
            elif ch == 'k':
                active -= 1

        if active != 0:
            return -1

        return max_frogs
