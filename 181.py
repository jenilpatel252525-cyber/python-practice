nums = [100, 200, 300, 400, 500, 600]
target = 300
count=0
res=[]

def find(i,curr):
    global count
    if len(curr)==len(nums) and sum(curr)==target:
        res.append(curr)
        count+=1
        return
    for j in range(i,len(nums)):
        find(j+1,curr+[nums[j]])
        find(j+1,curr+[-nums[j]])
        
find(0,[])

# print(count)
# print(res)







from functools import lru_cache

nums = [100, 200, 300, 400, 500, 600]
target = 300
count = 0

@lru_cache(maxsize=None)
def find(i, curr):
    global count
    if i == len(nums):
        if curr == target:
            count += 1
        return
    
    # Now safe to use nums[i]
    find(i + 1, curr + nums[i])
    find(i + 1, curr - nums[i])

# find(0, 0)
# print(count)
# 





def findTargetSumWays(nums, target):
    total = sum(nums)
    
    # Check for impossible case
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    
    subset_sum = (target + total) // 2
    
    # dp[i] = number of ways to reach sum i
    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # There's one way to make sum 0: use nothing

    for num in nums:
        for i in range(subset_sum, num - 1, -1):
            dp[i] += dp[i - num]
            print(dp)

    return dp[subset_sum]


nums = [1, 2, 3, 4, 5, 6]
target = 3
print(findTargetSumWays(nums, target))