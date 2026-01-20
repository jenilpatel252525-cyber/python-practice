import heapq

a=[1,1,1,2,2,3]

heap = []

k=2

b={}

c=[]

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
        
for key,val in b.items():
    heapq.heappush(heap,(-val,key))

for i in range(k):
    freq_neg, num = heapq.heappop(heap)
    c.append(num)
    
print(c)










from collections import defaultdict

def top_k_frequent(nums, k):
    freq = defaultdict(int)

    # Step 1: Count frequency — O(n)
    for num in nums:
        freq[num] += 1

    # Step 2: Bucket sort by frequency — O(n)
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Step 3: Gather k most frequent from buckets — O(n)
    result = []
    for i in range(n, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result