class Solution:
    def equationsPossible(self, equations):
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px

        # 1️⃣ Process all equality equations
        for eq in equations:
            if eq[1:3] == "==":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        # 2️⃣ Process all inequality equations
        for eq in equations:
            if eq[1:3] == "!=":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if find(a) == find(b):
                    return False

        return True

equations = ["a==b","b!=a"]