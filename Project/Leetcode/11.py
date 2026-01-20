a=[1,2,3,2,2]

def majorityElement(nums):
    # Initialize variables
    candidate = None
    count = 0
    
    # Iterate through the array
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate
