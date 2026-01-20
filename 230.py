nums = [10,5,2,6]

k=700

count=0

curr=0

prod=1

for i in range(len(nums)):
    flag=False
    if nums[i]<k:
        count+=1
    prod=prod*nums[i]
    if prod<k and prod!=nums[i]:
        count+=1
    while prod>=k:
        prod/=nums[curr]
        curr+=1
        flag=True
    if flag:
        count+=1
        
k=len(nums)-curr

j=(k*(k+1))/2 - (k) - (k-1)

count+=j

print(int(count))





nums = [10,5,2,6]
k = 700

prod = 1
count = 0
left = 0

for right in range(len(nums)):
    prod *= nums[right]
    while prod >= k and left <= right:
        prod //= nums[left]   # use // for integer division
        left += 1
    count += (right - left + 1)

print(count)   # 10
