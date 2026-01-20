from collections import Counter

def has_permutation(s1, s2):
    m, n = len(s2), len(s1)
    if n > m:
        return False

    need = Counter(s1)
    window = Counter(s2[:n])

    if window == need:
        return True

    for i in range(1, m - n + 1):
        # add new char (entering window)
        window[s2[i + n - 1]] += 1

        # remove old char (leaving window)
        old_char = s2[i - 1]
        window[old_char] -= 1
        if window[old_char] == 0:
            del window[old_char]

        if window == need:
            return True

    return False







def check_inclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False

    # frequency arrays for 'a' to 'z'
    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(n):
        count1[ord(s1[i]) - ord('a')] += 1
        count2[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        if count1[i] == count2[i]:
            matches += 1

    # sliding window over s2
    for i in range(n, m):
        if matches == 26:
            return True

        # char entering window
        idx_in = ord(s2[i]) - ord('a')
        count2[idx_in] += 1
        if count2[idx_in] == count1[idx_in]:
            matches += 1
        elif count2[idx_in] - 1 == count1[idx_in]:
            matches -= 1

        # char leaving window
        idx_out = ord(s2[i - n]) - ord('a')
        count2[idx_out] -= 1
        if count2[idx_out] == count1[idx_out]:
            matches += 1
        elif count2[idx_out] + 1 == count1[idx_out]:
            matches -= 1

    return matches == 26
