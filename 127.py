def combinationSum3(k, n):
    res = []

    def backtrack(start, path, total):
        if len(path) == k:
            if total == n:
                res.append(path[:])
            return
        for i in range(start, 10):
            if total + i > n:
                break  # pruning
            path.append(i)
            backtrack(i + 1, path, total + i)
            path.pop()  # backtrack

    backtrack(1, [], 0)
    return res