def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Step 1: Find first decreasing element from the end
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the element just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the part after index i
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
