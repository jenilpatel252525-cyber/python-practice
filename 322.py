words = ["abc","deq","mee","aqq","dkd","ccc"]

pattern = "abb"

class Solution:
    def findAndReplacePattern(self, words, pattern):
        
        def encode(s):
            mapping = {}
            code = []
            next_id = 1

            for ch in s:
                if ch not in mapping:
                    mapping[ch] = next_id
                    next_id += 1
                code.append(mapping[ch])

            return code
        
        pattern_code = encode(pattern)
        result = []

        for word in words:
            if encode(word) == pattern_code:
                result.append(word)

        return result
