def isOneBitCharacter(bits):
    i = 0
    n = len(bits)
    
    while i < n - 1:
        if bits[i] == 1:
            i += 2  # it's a two-bit character (10 or 11)
        else:
            i += 1  # it's a one-bit character (0)

    # If we stopped at the last index, it must be a one-bit character
    return i == n - 1
