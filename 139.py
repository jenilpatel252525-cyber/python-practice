class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        rows, cols = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build prefix sum matrix
        for r in range(rows):
            for c in range(cols):
                self.prefixSum[r+1][c+1] = (
                    matrix[r][c]
                    + self.prefixSum[r][c+1]
                    + self.prefixSum[r+1][c]
                    - self.prefixSum[r][c]  #because r,c is counted 2 times
                )

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.prefixSum[row2+1][col2+1]
            - self.prefixSum[row1][col2+1]
            - self.prefixSum[row2+1][col1]
            + self.prefixSum[row1][col1]  #because row1,col1 is deducted 2 times
        )

numMatrix = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])

print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12