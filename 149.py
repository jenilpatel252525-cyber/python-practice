a=[1,1,7, 4, 5, 5, 6, 3, 8, 2, 9, 1, 3, 0, 5, 2, 6, 3]
l=0

flag1=True
flag2=True

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        if flag1:
            if l==0:
                l=2
            else:
                l+=1
            flag1=False
            flag2=True
    elif a[i]>a[i+1]:
        if flag2:
            if l==0:
                l=2
            else:
                l+=1
            flag2=False
            flag1=True
            
print(l)










def wiggleMaxLength(nums):
    if not nums:
        return 0

    up = down = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1
        # if equal, skip

    return max(up, down)

a = [1, 7, 4, 5, 5, 6, 3, 8, 2, 9, 1, 3, 0, 5, 2, 6, 3]
print(wiggleMaxLength(a))  # Output: 15