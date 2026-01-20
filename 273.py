s="abababbc"

k=3

from collections import Counter

dp=[0]*len(s)

c=Counter(s)

for i in range(len(s)):
    dp[i]=c[s[i]]
    
ans=0
temp=0

for i in range(len(dp)):
    if dp[i]>=k:
        temp+=1
    else:
        ans=max(ans,temp)
        temp=0
        
print(ans if ans>=k else 0)











def longestSubstring(s, k):
    if not s:
        return 0
    
    c = Counter(s)
    for ch in c:
        if c[ch] < k:
            return max(longestSubstring(t, k) for t in s.split(ch))
    return len(s)

print(longestSubstring("aaabbccddeeeffgghhhiiijjjkkklllmmmnnn", 3))  # 36
