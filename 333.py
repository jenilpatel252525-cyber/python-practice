class Solution:
    def queryString(self, s: str, n: int) -> bool:
        found = set()
        max_len = len(bin(n)) - 2  # max bits needed

        for i in range(len(s)):
            if s[i] == '0':
                continue  # skip leading zero
            val = 0
            for j in range(i, min(i + max_len, len(s))):
                val = (val << 1) + (s[j] == '1')
                if val > n:
                    break
                found.add(val)

        return len(found) == n
