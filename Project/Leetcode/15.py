a=[1,5,0,3,4]

b=set()

for i in a:
    b.add(i)

for i in range(len(a)+1):
    if i not in b:
        print(i)

def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2  # Sum of numbers from 0 to n
    array_sum = sum(nums)  # Sum of elements in the array
    return total_sum - array_sum  # Missing number
