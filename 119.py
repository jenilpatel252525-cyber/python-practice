nums = [3,30,34,5,9]

def jenil(num,k):
    if num < 10^k:
        return 0.5
    r=num
    while num>=10^k:
        r=num%10
        num=num - r
        num=num/10
    return r

def com(num1,num2):
    k=0
    r1=jenil(num1,k)
    r2=jenil(num2,k)
    while r1==r2:
        k+=1
        r1=jenil(num1,k)
        r2=jenil(num2,k)
    
    if r2>r1:
        return num2
    else:
        return num1
    
print(int(com(12,120)))





from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

nums = [3, 30, 34, 5, 9]
nums = list(map(str, nums))

# Sort with custom comparator
nums.sort(key=cmp_to_key(compare))

# Edge case: when all numbers are 0
if nums[0] == '0':
    print("0")
else:
    print("".join(nums))
    
    
    
    
    
    
def compare(a, b):
    # Custom logic to decide which number should come first
    if a + b > b + a:
        return True  # a should come before b
    else:
        return False  # b should come before a

def largestNumber(nums):
    # Step 1: Convert to strings
    nums = list(map(str, nums))

    # Step 2: Manual bubble sort using compare
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Swap

    # Step 3: Handle edge case like [0, 0]
    if nums[0] == '0':
        return '0'

    # Step 4: Join and return result
    return ''.join(nums)

# Example
nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))  # Output: "9534330"
