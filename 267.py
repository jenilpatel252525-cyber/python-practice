class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        n = len(s)

        # Try all splits for first two numbers
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = s[:i], s[i:j]

                # skip numbers with leading zeros
                if (len(num1) > 1 and num1[0] == "0") or (len(num2) > 1 and num2[0] == "0"):
                    continue

                if self.check(num1, num2, s[j:]):
                    return True
        return False

    def check(self, num1, num2, remaining):
        while remaining:
            sum_str = str(int(num1) + int(num2))
            if not remaining.startswith(sum_str):
                return False
            # shift numbers
            num1, num2 = num2, sum_str
            remaining = remaining[len(sum_str):]
        return True
