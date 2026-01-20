s = "eleetminicoworoep"

def findTheLongestSubstring(s: str) -> int:
    pos = {0: -1}   # mask → earliest index
    mask = 0
    ans = 0

    vowels = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}

    for i, ch in enumerate(s):
        if ch in vowels:
            mask ^= (1 << vowels[ch])

        if mask in pos:
            ans = max(ans, i - pos[mask])
        else:
            pos[mask] = i

    return ans














def findTheLongestSubstring(s: str) -> int:
    first = [-2] * 32
    first[0] = -1

    mask = 0
    ans = 0

    for i, ch in enumerate(s):
        if ch == 'a': mask ^= 1 << 0
        elif ch == 'e': mask ^= 1 << 1
        elif ch == 'i': mask ^= 1 << 2
        elif ch == 'o': mask ^= 1 << 3
        elif ch == 'u': mask ^= 1 << 4

        if first[mask] != -2:
            ans = max(ans, i - first[mask])
        else:
            first[mask] = i

    return ans
