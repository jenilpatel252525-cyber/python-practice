def erase_overlap_intervals(intervals):
    # Step 1: Sort by end time
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            # No overlap, keep it
            prev_end = end
        else:
            # Overlap, remove this one
            count += 1

    return count
