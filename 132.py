def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num

    # Find any set bit (rightmost one)
    diff = xor & -xor  # isolates the rightmost 1-bit

    a = 0
    b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num

    return [a, b]
