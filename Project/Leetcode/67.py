# a=[4,5,6,7,0,1,2]

# target = 0

# low = 0

# high = len(a)-1

# def find(a,low,high,target):
#         if a[low]==target:
#              return low
#         if a[high]==target:
#              return high
    
#         if target<a[low] and target<a[high]:
#             mid=int((low+high)/2)
#             if a[mid]==target:
#                  return mid
#             low=mid
#             while a[low]<a[low+1]:
#                  low+=1
#             low+=1

#             while low<high:
#                 mid=int((low+high)/2)
#                 if a[mid]==target:
#                     return mid
#                 elif a[mid]>target:
#                     high=mid-1
#                 else:
#                     low=mid+1
#             return -1
        
#         else:
#             mid=int((low+high)/2)
#             if a[mid]==target:
#                  return mid
#             high=mid
#             while a[high]>a[high-1]:
#                  high-=1
#             high-=1
#             while low<high:
#                 mid=int((low+high)/2)
#                 if a[mid]==target:
#                     return mid
#                 else:
#                     high=mid-1
#             return -1
        
# print(find(a,low,high,target))


def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Check which side is sorted
        if nums[low] <= nums[mid]:  # Left side is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
