nums=[1,1,2,3,3,3,4,5,5]

# for i in a:
#     if a.count(i)>1:
#         a.remove(i)

# l2=len(a)

# i=l2

# while i < l1:
#     a.insert(i,"_")
#     i+=1

# print(a)

def removeDuplicates(nums):
    if not nums:
        return 0
    
    k = 1 
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]: # _ is dont care means any value
            nums[k] = nums[i]
            k += 1
    
    return k

print(removeDuplicates(nums))

print(nums)


