def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start a sequence if num-1 is not in the set
        if num - 1 not in num_set:
            current_num = num
            length = 1

            while current_num + 1 in num_set:
                current_num += 1
                length += 1

            longest = max(longest, length)

    return longest