nums = [5,4,0,3,1,6,2]

ans=0

visited=set()

for i in range(len(nums)):
    if nums[i] in visited:
        continue
    temp=set()
    visited.add(nums[i])
    temp.add(nums[i])
    next=nums[nums[i]]
    while next not in temp:
        visited.add(next)
        temp.add(next)
        next=nums[next]
    ans=max(ans,len(temp))
    
print(ans)





def arrayNesting(nums):
    n = len(nums)
    res = 0

    for i in range(n):
        length = 0
        while nums[i] != -1:  # -1 means visited
            temp = nums[i]
            nums[i] = -1  # mark as visited
            i = temp
            length += 1
        res = max(res, length)
    return res


# Example usage:
print(arrayNesting([5,4,0,3,1,6,2]))  # Output: 4
print(arrayNesting([0,1,2]))          # Output: 1