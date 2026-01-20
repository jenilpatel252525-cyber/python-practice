m=5
n=5

ops=[[2,4],[4,3],[3,5]]


def maxCount(m, n, ops):
    if not ops:
        return m * n

    min_a = min(op[0] for op in ops)
    min_b = min(op[1] for op in ops)

    return min_a * min_b

