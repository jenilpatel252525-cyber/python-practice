import math

matrix = [
    [1,5,7],
    [10,11,12],
    [12,13,15]
    ]

k=5

def kthSmallest(matrix, k):
    n = len(matrix)

    def count_less_equal(mid):
        # Start from bottom-left corner
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1  # All values in current column above this row are <= mid
                col += 1
            else:
                row -= 1
        return count

    left = matrix[0][0]
    right = matrix[-1][-1]

    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left
