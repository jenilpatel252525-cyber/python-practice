from collections import Counter

text = "aaabca"

curr=1

ans=0

count=Counter(text)

brek=0

count[text[0]]-=1

prev=[text[0]]

for i in range(1,len(text)):
    if text[i]==prev[0]:
        curr+=1
        count[text[i]]-=1
        ans=max(ans,curr)
    elif brek==0 and count[prev[0]]>0:
        brek+=1
        curr+=1
        count[text[i]]-=1
        ans=max(ans,curr)
    else:
        brek=0
        ans=max(ans,curr)
        curr=1
        prev.pop()
        prev.append(text[i])
        count[text[i]]-=1
        
if prev[0]==text[0] and brek==1:
    ans-=1
        
print(ans)













from collections import Counter

def maxRepOpt1(text: str) -> int:
    freq = Counter(text)
    n = len(text)

    # Step 1: build blocks (char, length)
    blocks = []
    i = 0
    while i < n:
        j = i
        while j < n and text[j] == text[i]:
            j += 1
        blocks.append((text[i], j - i))
        i = j

    ans = 0

    # Step 2: try all possibilities
    for i in range(len(blocks)):
        ch, length = blocks[i]

        # Case 1: extend single block by 1 if extra char exists
        ans = max(ans, min(length + 1, freq[ch]))

        # Case 2: merge two blocks separated by exactly one char
        if (
            i + 2 < len(blocks)
            and blocks[i + 1][1] == 1
            and blocks[i + 2][0] == ch
        ):
            merged = blocks[i][1] + blocks[i + 2][1]
            if freq[ch] > merged:
                merged += 1
            ans = max(ans, merged)

    return ans
