class Solution:
    def findLUSlength(self, strs):
        # Sort by descending length
        strs.sort(key=lambda x: len(x), reverse=True)

        def is_subsequence(a, b):
            # if lengths equal, must be identical
            if len(a) == len(b):
                for i in range(len(a)):
                    if a[i] != b[i]:
                        return False
                return True

        n = len(strs)
        for i in range(n):
            
            if i==n-1:
                if len(strs[i])<len(strs[i-1]):
                    return len(strs[i])
                else:
                    return -1
                
            s = strs[i]
            uncommon = True

            # check only with previous (longer or equal) strings
            for j in range(i+1,n):
                t=strs[j]
                if len(s)>len(t):
                    return len(s)
                else:
                    if is_subsequence(s,t):
                        uncommon=False
                if not uncommon:
                    break
                
            if uncommon:
                return len(s)

        return -1

print(Solution().findLUSlength(["aaa", "aa", "a"]))









class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        # Sort by descending length so we can stop early when we find the first uncommon
        strs.sort(key=len, reverse=True)

        def is_subsequence(a: str, b: str) -> bool:
            """Return True if a is a subsequence of b"""
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        n = len(strs)

        for i in range(n):
            # Skip duplicates — duplicates can never be uncommon
            if strs.count(strs[i]) > 1:
                continue

            s = strs[i]
            uncommon = True

            # Check if s is a subsequence of any longer or equal-length string
            for j in range(n):
                if i == j:
                    continue
                if len(strs[j]) < len(s):
                    break  # since list sorted descending, no need to check further
                if is_subsequence(s, strs[j]):
                    uncommon = False
                    break

            if uncommon:
                return len(s)

        return -1
