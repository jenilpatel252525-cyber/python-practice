def numSteps(s: str) -> int:
    steps = 0
    carry = 0
    n = len(s)

    for i in range(n - 1, 0, -1):
        bit = int(s[i])
        curr = bit + carry

        if curr % 2 == 1:     # odd
            steps += 2       # add 1 + shift
            carry = 1
        else:                # even
            steps += 1       # shift only

    return steps + carry



















def numSteps(s: str) -> int:
    steps = 0
    carry = 0

    for i in range(len(s) - 1, 0, -1):
        if s[i] == '0':
            steps += 1 if carry == 0 else 2
        else:  # s[i] == '1'
            steps += 2 if carry == 0 else 1
            carry = 1

    return steps + carry
