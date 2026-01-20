nums = [1,2,2,3,3,4,4,8,8]

def single(left,right):
    mid=(left+right)//2
    if right-left==2:
        if nums[mid]==nums[mid-1]:
            print(nums[mid+1])
        else:
            print(nums[mid-1])
        exit()
    if nums[mid]==nums[mid-1]:
        single(left,mid)
    elif nums[mid]==nums[mid+1]:
        single(mid,right)
    else:
        print(nums[mid])
        exit()
    
single(0,len(nums)-1)






nums = [1, 2, 2, 3, 3, 4, 4, 8, 8]

def single(left, right):
    if left == right:
        print(nums[left])
        return
    mid = (left + right) // 2
    if mid % 2 == 1:  # make mid even
        mid -= 1
    if nums[mid] == nums[mid + 1]:
        single(mid + 2, right)
    else:
        single(left, mid)

single(0, len(nums) - 1)




nums = [1, 2, 2, 3, 3, 4, 4, 8, 8]

def single(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        # Base case for 3 elements
        if right - left == 2:
            if nums[left] == nums[left + 1]:
                return nums[right]
            else:
                return nums[left]
        
        mid = (left + right) // 2
        
        # Make mid even
        if mid % 2 == 1:
            mid -= 1
        
        # Decide which half to keep
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    
    return nums[left]  # only one element left

print(single(nums))
