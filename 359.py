from collections import Counter

def minSteps(s: str, t: str) -> int:
    cnt = Counter(s)
    steps = 0

    for ch in t:
        if cnt[ch] > 0:
            cnt[ch] -= 1
        else:
            steps += 1

    return steps
