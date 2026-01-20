from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # Build the graph
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        # DFS function to find the path product
        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, value in graph[src].items():
                if neighbor not in visited:
                    res = dfs(neighbor, dst, visited)
                    if res != -1.0:
                        return res * value
            return -1.0

        results = []
        for num, den in queries:
            results.append(dfs(num, den, set()))
        return results
