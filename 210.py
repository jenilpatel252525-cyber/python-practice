nums = [4,2,3,4]

def isvalid(a):
    total=sum(a)
    for i in a:
        if i>=total-i:
            return False
    return True

curr=[]

count=0

def triangle(i):
    global curr
    global count
    if len(curr)>=3:
        if isvalid(curr):
            count+=1
        return
    for j in range(i,len(nums)):
        curr.append(nums[j])
        triangle(j+1)
        curr.pop()
        
triangle(0)

print(count)







def triangleNumber(nums):
    nums.sort()
    n = len(nums)
    count = 0

    for k in range(n - 1, 1, -1):  # fix largest side
        l, r = 0, k - 1
        while l < r:
            if nums[l] + nums[r] > nums[k]:
                count += (r - l)
                r -= 1
            else:
                l += 1
    return count



def triangleNumber_backtrack(nums):
    from itertools import combinations
    count = 0

    for a, b, c in combinations(nums, 3):
        if a + b > c and a + c > b and b + c > a:
            count += 1

    return count