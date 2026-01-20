a=[1,2,3,4,50,60,100]

def minMoves2(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)






import random

def quickselect(nums, k):
    if len(nums) == 1:
        return nums[0]

    pivot = random.choice(nums)

    lows = [el for el in nums if el < pivot]
    highs = [el for el in nums if el > pivot]
    pivots = [el for el in nums if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def minMoves2(nums):
    n = len(nums)
    median = quickselect(nums, n // 2)
    return sum(abs(num - median) for num in nums)