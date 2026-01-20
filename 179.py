nums = [3, 9, 1, 2, 3, 11, 5]

p1=[]
p2=[]

while len(nums)>0:
    
    if len(nums)<1:
        break
    
    if len(nums)>3:
        curr1=max(nums[1]-nums[0],nums[-1]-nums[0])
        curr2=max(nums[-2]-nums[-1],nums[0]-nums[-1])
        curr=min(curr1,curr2)
        if curr==curr1:
            p1.append(nums[0])
            nums.pop(0)
        else:
            p1.append(nums[-1])
            nums.pop()
    elif len(nums)>1:
        curr=max(nums[0],nums[-1])
        p1.append(curr)
        nums.remove(curr)
    else:
        p1.append(nums[0])
        nums.pop()
        
    if len(nums)<1:
        break
        
    if len(nums)>3:
        curr1=max(nums[1]-nums[0],nums[-1]-nums[0])
        curr2=max(nums[-2]-nums[-1],nums[0]-nums[-1])
        curr=min(curr1,curr2)
        if curr==curr1:
            p2.append(nums[0])
            nums.pop(0)
        else:
            p2.append(nums[-1])
            nums.pop()
    elif len(nums)>1:
        curr=max(nums[0],nums[-1])
        p2.append(curr)
        nums.remove(curr)
    else:
        p2.append(nums[0])
        nums.pop()
    
print(sum(p1)>=sum(p2))






nums = [3, 9, 1, 2, 3, 11, 5]
n = len(nums)

# Initialize DP table
dp = [[0] * n for _ in range(n)]

# Base case: only one number to choose from
for i in range(n):
    dp[i][i] = nums[i]

# Fill DP table for subarrays of length 2 to n
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        # Choose nums[i] or nums[j]
        pick_left = nums[i] - dp[i + 1][j]     # pick left end
        pick_right = nums[j] - dp[i][j - 1]    # pick right end
        dp[i][j] = max(pick_left, pick_right)  # max difference

# Final answer
winner = dp[0][n - 1] >= 0

# Print DP table
print("DP Table:")
for row in dp:
    print(row)

print("\nPlayer 1 can win?" , winner)