nums = [1,49,50]
moves=0

def increment_all_except(nums, skip_index):
    for i in range(len(nums)):
        if i != skip_index:
            nums[i] += 1

while max(nums)>min(nums):
    j=nums.index(max(nums))
    moves+=1
    increment_all_except(nums,j)
    
print(moves)



def min_moves(nums):
    return sum(nums) - len(nums) * min(nums)

# Example
nums = [1, 2, 3]
print(min_moves(nums))  # Output: 3