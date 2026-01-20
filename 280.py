s = "abcacdade"

count = {}
ans = []

for ch in s:
    if ch not in count:
        count[ch] = 1
        ans.append(ch)
    else:
        count[ch] += 1
        if len(ans) > 1:
            j = ans.index(ch)  # old position
            k = j
            while k > 0 and count[ch] > count[ans[k-1]]:
                k -= 1
            del ans[j]
            ans.insert(k, ch)

# build final string
res = "".join(ch * count[ch] for ch in ans)

print("Frequencies:", count)
print("Order of chars by frequency:", ans)
print("Final frequency-sorted string:", res)











from collections import Counter

def frequencySort(s: str) -> str:
    # Step 1: count frequencies
    freq = Counter(s)   # O(n)
    
    # Step 2: make buckets (size = max frequency + 1)
    max_freq = max(freq.values())
    buckets = [[] for _ in range(max_freq + 1)]
    
    for ch, f in freq.items():
        buckets[f].append(ch)
    
    # Step 3: build result from high freq to low
    res = []
    for f in range(max_freq, 0, -1):
        for ch in buckets[f]:
            res.append(ch * f)
    
    return "".join(res)
