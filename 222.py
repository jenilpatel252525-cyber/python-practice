def checkPossibility(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count += 1
            if count > 1:
                return False
            # Decide which element to modify
            if i == 0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]  # lower nums[i]
            else:
                nums[i+1] = nums[i]  # raise nums[i+1]
    return True
