a= [3,2,3,1,2,4,5,5,6]

k = 4

s=[]

for i in range(len(a)):
    if len(s)==0:
        s.append(a[i])
        continue
    for j in range(len(s)):
        if a[i]>s[j]:
            s.insert(j,a[i])
            break
    if len(s)<i+1:
        s.append(a[i])
        
print(s[k-1])





import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
    return heap[0]





import random

def quickselect(nums, k):
    # kth largest means index = len(nums) - k
    k = len(nums) - k
    
    def select(left, right):
        pivot_index = random.randint(left, right)
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        pivot = nums[right]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to its final place
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        # Check the pivot position
        if store_index == k:
            return nums[store_index]
        elif store_index < k:
            return select(store_index + 1, right)
        else:
            return select(left, store_index - 1)
    
    return select(0, len(nums) - 1)
