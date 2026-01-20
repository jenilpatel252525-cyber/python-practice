def arrayPairSum(nums):
    # Step 1: Sort the array
    nums.sort()

    # Step 2: Sum every first element of each pair (i.e., every even index)
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum

# Example usage:
nums1 = [1, 4, 3, 2]
print(arrayPairSum(nums1))  # Output: 4

nums2 = [6, 2, 6, 5, 1, 2]
print(arrayPairSum(nums2))  # Output: 9
