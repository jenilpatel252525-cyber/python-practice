nums1 = [1,7,11]

nums2 = [2,4,6]

i=0
j=0
curr1=1
curr2=1
ans=[[nums1[0],nums2[0]]]

while i<len(nums1) and j<len(nums2):
    if nums1[i]+nums2[curr2]<=nums1[curr1]+nums2[j]:
        ans.append([nums1[i],nums2[curr2]])
        curr2+=1
        if curr2>=len(nums2):
            i+=1
            curr2=0
    else:
        ans.append([nums1[curr1],nums2[j]])
        curr1+=1
        if curr1>=len(nums1):
            j+=1
            curr1=0

seen = set()
result = []

for pair in ans:
    key = tuple(sorted(pair))  # Ensure (1,4) and (4,1) are the same
    if key not in seen:
        seen.add(key)
        result.append(pair)  # Keep original order

print(result)








import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    min_heap = []
    visited = set()
    result = []

    # Start with the smallest pair (0, 0)
    heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
    visited.add((0, 0))

    while min_heap and len(result) < k:
        total, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        # Move right: (i, j + 1)
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))

        # Move down: (i + 1, j)
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))

    return result