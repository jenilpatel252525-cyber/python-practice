def breakPalindrome(s: str) -> str:
    n = len(s)
    if n == 1:
        return ""

    s = list(s)
    left, right = 0, n - 1

    while left < right and s[left] == 'a':
        left += 1
        right -= 1

    if left < right:
        s[left] = 'a'
    else:
        s[-1] = 'b'

    return "".join(s)





def breakPalindrome(s: str) -> str:
    n = len(s)
    if n == 1:
        return ""

    s = list(s)

    for i in range(n // 2):
        if s[i] != 'a':
            s[i] = 'a'
            return "".join(s)

    # all first-half chars are 'a'
    s[-1] = 'b'
    return "".join(s)
