class Solution:
    def splitIntoFibonacci(self, s: str):
        res = []
        n = len(s)
        MAX = 2**31 - 1

        def backtrack(index):
            if index == n and len(res) >= 3:
                return True

            num = 0
            for i in range(index, n):
                # leading zero check
                if i > index and s[index] == '0':
                    break

                num = num * 10 + int(s[i])
                if num > MAX:
                    break

                if len(res) >= 2:
                    if num < res[-1] + res[-2]:
                        continue
                    if num > res[-1] + res[-2]:
                        break

                res.append(num)
                if backtrack(i + 1):
                    return True
                res.pop()

            return False

        backtrack(0)
        return res
