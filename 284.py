class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1  # "122" → only one '1' in first 3
        
        s = [1, 2, 2]
        head = 2
        num = 1
        
        while len(s) < n:
            s.extend([num] * s[head])
            num = 3 - num  # flip 1 ↔ 2
            head += 1
        
        return s[:n].count(1)
