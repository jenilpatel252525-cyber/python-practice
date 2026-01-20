nums = [3,1,4,1,5]

k=2

checked=set()

ans=set()

for i in range(len(nums)):
    if nums[i]+k in checked:
        ans.add((nums[i],nums[i]+k))
    if nums[i]-k in checked:
        ans.add((nums[i],nums[i]-k))
    checked.add(nums[i])
    
print(ans)