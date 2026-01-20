a=[2,1,6,3,8,10,5]
b=set(a)
c=[]

max=a[0]
min=a[0]

for i in a:
    if i>max:
        max=i

for i in a:
    if i<min:
        min=i

for i in range(min,max+1):
    if i in b:
        continue
    else:
        c.append(i)

print(c)





def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]  # mark as visited

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
