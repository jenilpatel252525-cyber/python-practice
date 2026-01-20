s="abcabac"
s1=""

for i in range(len(s)-1,-1,-1):
    s1+=s[i]
    
dp=[[0]*(len(s)+1) for i in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(s)):
        if s[i]==s1[j]:
            dp[i+1][j+1]=1+dp[i][j]
        else:
            dp[i+1][j+1]=0
            
for i in range(len(s)+1):
    print(dp[i])
    
    
    
    
    
    
    
    
def all_palindromes(s: str):
    n = len(s)
    res = []

    def expand(l: int, r: int):
        while l >= 0 and r < n and s[l] == s[r]:
            res.append(s[l:r+1])   # collect the palindrome substring
            l -= 1
            r += 1

    for i in range(n):
        expand(i, i)       # odd
        expand(i, i + 1)   # even

    return res









class SolutionDP:
    # LeetCode 647 answer: count palindromic substrings
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # i from n-1 down to 0
        for i in range(n - 1, -1, -1):
            # j from i to n-1
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        # length 1 or 2
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    count += 1

        return count

    # Helper: list ALL palindromic substrings (with duplicates)
    def listPalindromes(self, s: str):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = []

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    res.append(s[i:j + 1])

        return res