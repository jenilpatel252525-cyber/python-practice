a= [1,2,3]

target = 4

count=0

curr=0

def find():
    global curr,count
    if curr>target:
        return
    if curr==target:
        count+=1
    for i in range(len(a)):
        curr+=a[i]
        find()
        curr-=a[i]
        
find()

print(count)






def combinationSum4_topdown(nums, target):
    memo = {}

    def dfs(curr):
        if curr > target:
            return 0
        if curr == target:
            return 1
        if curr in memo:
            return memo[curr]

        total = 0
        for num in nums:
            total += dfs(curr + num)

        memo[curr] = total
        return total

    return dfs(0)

# Example usage
a = [1, 2, 3]
target = 4
print(combinationSum4_topdown(a, target))  # Output: 7





def combinationSum4_bottomup(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # 1 way to make 0

    for total in range(1, target + 1):
        for num in nums:
            if total - num >= 0:
                dp[total] += dp[total - num]

    return dp[target]

# Example usage
a = [1, 2, 3]
target = 4
print(combinationSum4_bottomup(a, target))  # Output: 7