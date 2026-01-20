def findMinDifference(timePoints):
    # Convert to [hour, minute] pairs
    time_arr = [list(map(int, t.split(':'))) for t in timePoints]

    # Sort by hour, then minute
    time_arr.sort(key=lambda x: (x[0], x[1]))

    def diff(t1, t2):
        # Calculate minutes difference between two time points
        h1, m1 = t1
        h2, m2 = t2
        return (h2 - h1) * 60 + (m2 - m1)

    min_diff = 1440  # max minutes in a day
    n = len(time_arr)

    for i in range(n - 1):
        # Check difference between adjacent times
        min_diff = min(min_diff, diff(time_arr[i], time_arr[i + 1]))

    # Check difference between last and first (across midnight)
    # e.g., from 23:59 to 00:00 → 1 minute
    first = time_arr[0]
    last = time_arr[-1]
    across_midnight = 1440 - diff(first, last)
    min_diff = min(min_diff, across_midnight)

    return min_diff

# Examples:
print(findMinDifference(["23:59", "00:00"]))          # Output: 1
print(findMinDifference(["00:00", "23:59", "00:00"])) # Output: 0







def findMinDifference(timePoints):
    if len(timePoints) > 1440:
        # Pigeonhole principle: duplicates must exist
        return 0

    minutes_seen = [False] * 1440

    def to_minutes(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    for t in timePoints:
        m = to_minutes(t)
        if minutes_seen[m]:
            return 0  # duplicate found
        minutes_seen[m] = True

    prev = None
    first = None
    min_diff = 1440
    for i in range(1440):
        if minutes_seen[i]:
            if prev is not None:
                min_diff = min(min_diff, i - prev)
            else:
                first = i
            prev = i

    # Wrap-around difference
    min_diff = min(min_diff, 1440 - prev + first)
    return min_diff

# Examples:
print(findMinDifference(["23:59", "00:00"]))          # 1
print(findMinDifference(["00:00", "23:59", "00:00"])) # 0