class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def count_strings(remaining):
            return 1 << remaining  # 2^remaining

        ans = []
        prev = None

        for i in range(n):
            for ch in ['a', 'b', 'c']:
                if ch == prev:
                    continue

                remaining = n - i - 1
                cnt = count_strings(remaining)

                if k > cnt:
                    k -= cnt
                else:
                    ans.append(ch)
                    prev = ch
                    break
            else:
                return ""  # k too large

        return "".join(ans)
