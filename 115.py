a=[7, 1, 2, 3, 4, 5, 6] 

low=0

high=len(a)-1

ans=float("inf")

def find(a, low, high):
    if low > high:
        return float('inf')  # neutral for min
    mid = (low + high) // 2
    left_min = find(a, low, mid - 1)
    right_min = find(a, mid + 1, high)
    return min(a[mid], left_min, right_min)


def findMin(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # Minimum must be in the unsorted part
        if nums[mid] > nums[high]:
            # Minimum is to the right of mid
            low = mid + 1
        else:
            # Minimum is at mid or to the left
            high = mid

    return nums[low]