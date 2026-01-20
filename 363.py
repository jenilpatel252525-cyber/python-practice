from collections import Counter

def canConstruct(s: str, k: int) -> bool:
    if k > len(s):
        return False

    odd = sum(v % 2 for v in Counter(s).values())
    return odd <= k
