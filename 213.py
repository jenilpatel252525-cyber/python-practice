def maxDistance(arrays):
    res = 0
    # initialize with the first array
    min_val = arrays[0][0]
    max_val = arrays[0][-1]

    for i in range(1, len(arrays)):
        first = arrays[i][0]
        last = arrays[i][-1]

        # possible max distance with previous global min/max
        res = max(res, abs(last - min_val), abs(max_val - first))

        # update global min and max
        min_val = min(min_val, first)
        max_val = max(max_val, last)

    return res