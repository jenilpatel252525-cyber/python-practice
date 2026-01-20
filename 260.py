nums = [3,30,34,5,9]

from functools import cmp_to_key

def largestNumber(nums):
    # Convert numbers to strings for concatenation comparison
    nums = list(map(str, nums))
    
    # Custom comparator
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    # Sort with custom comparator
    nums.sort(key=cmp_to_key(compare))
    
    # Join results
    result = ''.join(nums)
    
    # Edge case: if result starts with '0', then all are zeros
    return '0' if result[0] == '0' else result


# Example tests
print(largestNumber([10, 2]))       # "210"
print(largestNumber([3, 30, 34, 5, 9]))  # "9534330"










def largestNumber(nums):
    nums = list(map(str, nums))
    
    def quicksort(arr, left, right):
        if left >= right:
            return
        pivot = arr[(left + right) // 2]
        i, j = left, right

        while i <= j:
            while i <= j and arr[i] + pivot > pivot + arr[i]:
                i += 1
            while i <= j and pivot + arr[j] > arr[j] + pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        quicksort(arr, left, j)
        quicksort(arr, i, right)

    # Sort using our quicksort
    quicksort(nums, 0, len(nums) - 1)

    result = ''.join(nums)
    return '0' if result[0] == '0' else result


# Example tests
print(largestNumber([10, 2]))            # "210"
print(largestNumber([3, 30, 34, 5, 9]))  # "9534330"
print(largestNumber([99, 9009]))         # "999009"
print(largestNumber([34, 3]))            # "3433"