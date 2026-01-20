def canJumpRecursiveForward(nums, start=0):
    n = len(nums)
    
    i = start
    while i < n - 1:
        if nums[i] == 0:
            zero_index = i
            can_jump_over = False
            
            # check in current segment from start to zero_index
            for j in range(start, zero_index):
                if j + nums[j] > zero_index:
                    can_jump_over = True
                    break
            
            if not can_jump_over:
                return False
            
            # recurse from zero_index
            return canJumpRecursiveForward(nums, zero_index)
        
        i += 1
    
    return True

# def canJump(nums):
#     maxReach = 0
#     for i in range(len(nums)):
#         if i > maxReach:
#             return False
#         maxReach = max(maxReach, i + nums[i])
#     return True
