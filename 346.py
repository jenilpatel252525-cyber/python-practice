s = "cba"

pairs = [[0,1],[1,2]]

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs):
        n = len(s)
        dsu = DSU(n)

        # 1️⃣ Union indices
        for a, b in pairs:
            dsu.union(a, b)

        # 2️⃣ Group indices by root
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[dsu.find(i)].append(i)

        # 3️⃣ Build result
        res = list(s)
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)
            indices.sort()
            for i, c in zip(indices, chars):
                res[i] = c

        return "".join(res)
