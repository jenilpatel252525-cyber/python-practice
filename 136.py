a=[3,1,3,4,2]

n=len(a)-1

s1=(n(n+1))/2

s2=sum(a)

print(s2-s1)







def findDuplicate(nums):
    # Phase 1: Finding the intersection point in the cycle
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]       # move one step
        hare = nums[nums[hare]]         # move two steps
        if tortoise == hare:
            break

    # Phase 2: Find the entrance to the cycle (duplicate number)
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare

# Example usage:
nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))  # Output: 3
