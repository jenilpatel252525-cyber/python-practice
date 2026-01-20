class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        seen = set()
        
        mask = 0
        full_mask = (1 << k) - 1
        
        for i in range(len(s)):
            # shift left and add current bit
            mask = ((mask << 1) & full_mask) | (s[i] == '1')
            
            if i >= k - 1:
                seen.add(mask)
                if len(seen) == needed:
                    return True
        
        return False










from collections import deque

def hasAllCodes(s, k):
    window = deque()
    seen = set()
    
    for ch in s:
        window.append(ch)
        if len(window) > k:
            window.popleft()
        if len(window) == k:
            seen.add(''.join(window))
    
    return len(seen) == (1 << k)
