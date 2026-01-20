class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        
        # Count vowels in the first window
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        
        ans = curr
        
        # Slide the window
        for r in range(k, len(s)):
            if s[r] in vowels:
                curr += 1
            if s[r - k] in vowels:
                curr -= 1
            
            ans = max(ans, curr)
        
        return ans
