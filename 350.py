from collections import Counter

s = "QQQQWWEERRRRQWEERQQR"

c=Counter(s)

excess={'Q':0,'R':0,'W':0,'E':0}

n=len(s)//4

for key,val in c.items():
    if val>n:
        excess[key]=val-n
        
l=0
r=0

ans = len(s)

current={}

for key in excess.keys():
    current[key]=0

while r<len(s) and l<=r:
    current[s[r]]+=1
    while current[s[l]]>excess[s[l]] and l<r:
        current[s[l]]-=1
        l+=1
    # check if desired excessive chars fall in this range and make answer length
    if all(current[ch] >= excess[ch] for ch in excess):
        ans = min(ans, r - l + 1)
    r+=1
    
print(ans)
















from collections import Counter

s = "QQQQWWEERRRRQWEERQQR"

c = Counter(s)
excess = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}

target = len(s) // 4

for ch in excess:
    if c[ch] > target:
        excess[ch] = c[ch] - target

l = 0
ans = len(s)
current = {ch: 0 for ch in excess}

for r in range(len(s)):
    current[s[r]] += 1

    # shrink only when window is valid
    while all(current[ch] >= excess[ch] for ch in excess):
        ans = min(ans, r - l + 1)
        current[s[l]] -= 1
        l += 1

print(ans)
