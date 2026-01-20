def findRightInterval(intervals):
    n = len(intervals)
    
    # Step 1: Store (start, original_index) pairs
    starts = [(interval[0], i) for i, interval in enumerate(intervals)]
    
    # Step 2: Sort based on start values
    starts.sort()
    
    # Manual binary search function
    def binary_search(target):
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if starts[mid][0] >= target:
                ans = starts[mid][1]
                right = mid - 1  # Look for smaller valid start
            else:
                left = mid + 1
        return ans
    
    # Step 3: For each interval, find right interval
    result = []
    for interval in intervals:
        end = interval[1]
        result.append(binary_search(end))
    
    return result