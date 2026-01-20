def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:  # no overlap
            merged.append(interval)
        else:  # overlap
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged



def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Step 1: Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)  # Add the merged interval

    # Step 3: Add the rest of the intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
