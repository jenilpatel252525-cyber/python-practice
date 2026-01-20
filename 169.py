nums = [3,1,4,2]

def find132pattern(nums):
    stack = []
    third = float('-inf')  # Represents nums[k]

    for i in reversed(range(len(nums))):
        if nums[i] < third:
            return True  # nums[i] < nums[k] < nums[j]
        while stack and nums[i] > stack[-1]:
            third = stack.pop()  # Update possible nums[k]
        stack.append(nums[i])

    return False

left=0
right=len(nums)-1