class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = []

        while A > 0 or B > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                # must place the other character
                if res[-1] == 'a':
                    res.append('b')
                    B -= 1
                else:
                    res.append('a')
                    A -= 1
            else:
                # place the one with larger count
                if A >= B:
                    res.append('a')
                    A -= 1
                else:
                    res.append('b')
                    B -= 1

        return "".join(res)




class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        # Decide major and minor
        if A >= B:
            major, minor = 'a', 'b'
            major_cnt, minor_cnt = A, B
        else:
            major, minor = 'b', 'a'
            major_cnt, minor_cnt = B, A

        res = []

        if minor_cnt == 0:
            # Only majors left → at most 2 allowed
            return major * min(2, major_cnt)

        ratio = major_cnt / minor_cnt
        base = int(ratio)              # floor part
        frac = ratio - base            # fractional part
        carry = 0.0

        while major_cnt > 0 or minor_cnt > 0:

            # 🔴 Safety rule: prevent 3 in a row
            if len(res) >= 2 and res[-1] == res[-2]:
                if res[-1] == major and minor_cnt > 0:
                    res.append(minor)
                    minor_cnt -= 1
                elif major_cnt > 0:
                    res.append(major)
                    major_cnt -= 1
                continue

            # Place base number of majors (max 2!)
            for _ in range(min(base, 2)):
                if major_cnt > 0:
                    res.append(major)
                    major_cnt -= 1

            # Accumulate fractional part
            carry += frac
            if carry >= 1 and major_cnt > 0:
                # Extra major allowed
                if len(res) < 2 or res[-1] != res[-2]:
                    res.append(major)
                    major_cnt -= 1
                    carry -= 1

            # Place one minor if available
            if minor_cnt > 0:
                res.append(minor)
                minor_cnt -= 1

        return "".join(res)
