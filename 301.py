import math

def build_lps(p: str) -> list[int]:
    n = len(p)
    lps = [0] * n
    j = 0  # length of previous longest prefix suffix

    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = lps[j - 1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps


def kmp_search(text: str, pattern: str) -> bool:
    if not pattern:
        return True
    if not text:
        return False

    lps = build_lps(pattern)
    j = 0  # index in pattern

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return True
    return False


def repeatedStringMatch(a: str, b: str) -> int:
    # Quick necessary check: chars in b must be in a
    if not set(b).issubset(set(a)):
        return -1

    n, m = len(a), len(b)
    k = math.ceil(m / n)

    # 1) Try k repeats
    s1 = a * k
    if kmp_search(s1, b):
        return k

    # 2) Try k+1 repeats
    s2 = a * (k + 1)
    if kmp_search(s2, b):
        return k + 1

    # Optional: some people also check k+2 to be super safe
    s3 = a * (k + 2)
    if kmp_search(s3, b):
        return k + 2

    return -1








import math

def repeatedStringMatch(a: str, b: str) -> int:
    # Quick necessary check: chars in b must be in a
    if not set(b).issubset(set(a)):
        return -1

    n, m = len(a), len(b)
    k = math.ceil(m / n)

    repeated = a * k
    if b in repeated:
        return k

    repeated_plus_1 = a * (k + 1)
    if b in repeated_plus_1:
        return k + 1

    # (Optional) some people also test k+2; usually not needed but safe:
    repeated_plus_2 = a * (k + 2)
    if b in repeated_plus_2:
        return k + 2

    return -1