nums = [100]
ans=0

for i in range(len(nums)):
    count=len(nums)-1
    j=i
    k=0
    c=0
    while k<=count:
        temp=k*nums[j]
        c+=temp
        k+=1
        if j<count:
            j+=1
        else:
            j=0
    ans=max(c,ans)
    
print(ans)







nums = [100]

n = len(nums)
total_sum = sum(nums)
F = sum(i * num for i, num in enumerate(nums))
ans = F

for k in range(1, n):
    F = F + total_sum - n * nums[-k]
    ans = max(ans, F)

print(ans)