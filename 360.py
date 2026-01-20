from collections import defaultdict

s = "aabbcc"

count = defaultdict(int)

ans=0

l=0

left=0

for r in range(len(s)):
    flag=False
    count[s[r]] += 1
    print(count)

    while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
        count[s[l]] -= 1
        l += 1
        flag=True
        
    if flag:
        l-=1
        ans+=1+(l-left + len(s)-r-1)
        ans+=(l-left)*(len(s)-r-1)
        l+=1
        left=l
        
print(ans)











from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        l = 0
        ans = 0
        n = len(s)

        for r in range(n):
            count[s[r]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - r
                count[s[l]] -= 1
                l += 1

        return ans

sol=Solution()
print(sol.numberOfSubstrings(s))