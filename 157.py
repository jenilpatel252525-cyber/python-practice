a=[1, 3, 5, 7, 9, 10, 11, 12]
start=0
end=0
diff=0
i=0
l=0
count=0

while i < len(a)-1:
    if start==end:
        end=i+1
        diff=a[end]-a[start]
        l=2
        i+=1
        continue
    if a[i+1]-a[i]==diff:
        end=i+1
        l+=1
        i+=1
    else:
        if l>2:
            n=l-2
            count+=(n*(n+1))//2
        start=end
        
if l>2:
    n=l-2
    count+=(n*(n+1))//2
        
print(count)








def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3:
        return 0

    total = 0
    curr = 0  # counts valid slices ending at current position

    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            curr += 1
            total += curr
        else:
            curr = 0  # reset count if current 3 don't form arithmetic seq

    return total