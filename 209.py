nums = [1, 3, 5, 4, 2, 6]

ans=0

start=-1
curr=-float("inf")
idx=-1

for i in range(len(nums)-1):
    if nums[i]<=nums[i+1]:
        continue
    else:
        if start==-1:
            start=i
        if nums[i]>=curr:
            idx=i
            curr=nums[i]
        
i=0

while i<len(nums):
    if nums[i]>=curr and i!=idx:
        break
    i+=1
    
print(i-start if start!=-1 else 0)



def findUnsortedSubarray(nums):
    n = len(nums)
    left, right = 0, n - 1

    # Step 1: find initial left boundary
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1

    # already sorted
    if left == n - 1:
        return 0

    # Step 2: find initial right boundary
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    # Step 3: find min and max in disorder region
    sub_min = min(nums[left:right + 1])
    sub_max = max(nums[left:right + 1])

    # Step 4: expand left boundary
    while left > 0 and nums[left - 1] > sub_min:
        left -= 1

    # Step 5: expand right boundary
    while right < n - 1 and nums[right + 1] < sub_max:
        right += 1

    return right - left + 1