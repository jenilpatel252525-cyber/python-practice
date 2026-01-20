nums = [1,3,2,7,8,2,3,4,1,8,4]
for i in range(len(nums)):
    a, b = i, nums[i]-1
    nums[a], nums[b] = nums[b], nums[a]
    
print(nums)
    
ans=set()

while i < len(nums):
    correct_index = nums[i] - 1
    if 1 <= nums[i] <= len(nums) and nums[i] != nums[correct_index]:
        nums[i], nums[correct_index] = nums[correct_index], nums[i]
    else:
        i += 1

    
print(ans)


nums = [10, 3, 6, 4, 1, 9, 2, 7, 5, 8, 10, 3, 6, 4, 1, 9, 2, 7, 5, 8]
res = []

for i in range(len(nums)):
    index = abs(nums[i]) - 1
    if nums[index] < 0:
        res.append(abs(nums[i]))
    else:
        nums[index] *= -1

print(res)
