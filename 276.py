s = "AABABBAAACCCCDDDEEEFFFGGGHHHIIIIJJJKLMMMNNN"

k = 3

def characterReplacement_bruteforce(s: str, k: int) -> int:
    n = len(s)
    ans = 0
    i = 0
    
    while i < n:
        ch = s[i]   # pick streak char
        j = i
        changes = 0
        l = -1

        while j < n:
            if s[j] != ch:
                changes += 1
                if changes == 1:
                    l = j   # first mismatch
                if changes > k:
                    break
            j += 1

        ans = max(ans, j - i)
        if l == -1:   # no mismatches found
            break
        i = l   # restart from first mismatch

    return ans





def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict
    count = defaultdict(int)
    
    left = 0
    max_freq = 0
    ans = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        print(count)
        max_freq = max(max_freq, count[s[right]])
        
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

characterReplacement(s,k)