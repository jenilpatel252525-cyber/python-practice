from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str):
        @lru_cache(None)
        def ways(expr):
            res = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:  # '*'
                                res.append(l * r)
            if not res:  # only number
                res.append(int(expr))
            return res
        
        return ways(expression)
