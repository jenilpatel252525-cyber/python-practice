def checkSubarraySum(nums, k):
    remainder_index = {0: -1}  # remainder -> earliest index
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        if k != 0:
            prefix_sum %= k
        
        if prefix_sum in remainder_index:
            if i - remainder_index[prefix_sum] > 1:
                return True
        else:
            remainder_index[prefix_sum] = i

    return False
