nums = [1,2,1,3,5,6,4]

def findPeakElement(nums):
    low, high = 0, len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
            
    return low  # or high, both are equal here

def findPeakElement(nums):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        left = nums[mid - 1] if mid > 0 else float('-inf')
        right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
        
        if nums[mid] > left and nums[mid] > right:
            return mid  # found peak
        elif nums[mid] < left:
            high = mid - 1  # peak must be to the left
        else:
            low = mid + 1   # peak must be to the right