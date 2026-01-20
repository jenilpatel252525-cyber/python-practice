from collections import Counter

strs = ["eat","tea","tan","ate","nat","bat"]

ans={}

for i in strs:
    c=Counter(i)
    temp=frozenset(c)
    if temp in ans:
        ans[temp].append(i)
    else:
        ans[temp]=[i]
        
print(tuple(ans.values()))