class NumArray:

    def __init__(self, nums):
        self.prefixSum = [0]
        for num in nums:
            self.prefixSum.append(self.prefixSum[-1] + num)

    def sumRange(self, left, right):
        return self.prefixSum[right + 1] - self.prefixSum[left]


n1=NumArray([1,2,3,4])

