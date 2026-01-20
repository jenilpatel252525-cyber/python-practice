class Solution:
    def camelMatch(self, queries, pattern):
        res = []

        for q in queries:
            i = j = 0  # i → query, j → pattern
            ok = True

            while i < len(q):
                if j < len(pattern) and q[i] == pattern[j]:
                    i += 1
                    j += 1
                elif q[i].islower():
                    i += 1
                else:
                    ok = False
                    break

            if j < len(pattern):
                ok = False

            res.append(ok)

        return res
