a=[0,1,2,2,3,0,4,2]
b=[]
key=2

def removeElement(nums, val):
    # i = 0
    # n = len(nums)
    
    # while i < n:
    #     if nums[i] == val:
    #         nums[i] = nums[n - 1]  # Swap with the last element
    #         n -= 1                 # Reduce the size to check
    #     else:
    #         i += 1
    
    # return n

    k=0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


print(removeElement(a,key),a)