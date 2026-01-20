class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        
        words.sort(key=len)   # stable sort
        
        words[0] = words[0].capitalize()
        return " ".join(words)








class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        
        max_len = 0
        for w in words:
            max_len = max(max_len, len(w))
        
        # buckets where index = word length
        buckets = [[] for _ in range(max_len + 1)]
        
        for w in words:
            buckets[len(w)].append(w)
        
        res = []
        for length in range(1, max_len + 1):
            for w in buckets[length]:
                res.append(w)
        
        res[0] = res[0].capitalize()
        return " ".join(res)













