nums = [5,2,1,5,10,8,7,6]

amount=0

curr=0

def rob(j):
    global amount
    global curr
    curr+=nums[j]
    if j==len(nums)-1 or j==len(nums)-2:
        amount=max(amount,curr)
        return
    for i in range(j+2,len(nums)):
        rob(i)
        curr-=nums[i]
        
rob(0)        

print(amount)





def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev1 = 0  # max money up to house i - 1
    prev2 = 0  # max money up to house i - 2

    for num in nums:
        temp = prev1
        prev1 = max(prev1, prev2 + num)
        prev2 = temp

    return prev1