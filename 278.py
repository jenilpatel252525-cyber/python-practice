s = "cbaebabacd"

p = "abc"

from collections import Counter

def findAnagrams(s, p):
    p_count = Counter(p)
    res = []
    for i in range(len(s) - len(p) + 1):
        if Counter(s[i:i+len(p)]) == p_count:
            res.append(i)
    return res

# Example
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # Output: [0, 6]










from collections import Counter

def findAnagrams(s, p):
    p_count = Counter(p)
    window_count = Counter()
    res = []
    l = 0  # left pointer

    for r in range(len(s)):
        window_count[s[r]] += 1

        # shrink window if size > len(p)
        if r - l + 1 > len(p):
            window_count[s[l]] -= 1
            if window_count[s[l]] == 0:
                del window_count[s[l]]
            l += 1

        if window_count == p_count:
            res.append(l)

    return res

# Example
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # Output: [0, 6]
















def findAnagrams(s, p):
    res = []
    if len(p) > len(s):
        return res

    p_count = [0] * 26
    window = [0] * 26

    # fill p_count
    for ch in p:
        p_count[ord(ch) - ord('a')] += 1

    # initialize the first window
    for ch in s[:len(p)]:
        window[ord(ch) - ord('a')] += 1

    if window == p_count:
        res.append(0)

    # slide the window
    for i in range(len(p), len(s)):
        # add new char
        window[ord(s[i]) - ord('a')] += 1
        # remove old char
        window[ord(s[i - len(p)]) - ord('a')] -= 1

        if window == p_count:
            res.append(i - len(p) + 1)

    return res

# Example
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # Output: [0, 6]
