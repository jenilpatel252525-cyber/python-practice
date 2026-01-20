nums = [1,1,1]

k=2

s={0: 1}

ans=0

curr=0

for i in range(len(nums)):
    curr+=nums[i]
    if curr-k in s:
        ans+=s[curr-k]
    s[curr]=s.get(curr,0)+1
        
print(ans)








nums = [1, 1, 1]
k = 2

prefix_count = {0: 1}  # prefix sum 0 occurs once initially
curr_sum = 0
ans = 0

for num in nums:
    curr_sum += num
    if curr_sum - k in prefix_count:
        ans += prefix_count[curr_sum - k]
    prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

print(ans)  # Output: 2