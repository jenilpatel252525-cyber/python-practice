a=[1,2,3,4,5,6,10,11]
key=8

# low=0
# high=len(a)-1
# mid=0
# i=1

# while True:
#     mid=int((low+high)/2)
#     print("after",i)
#     print("low:",low)
#     print("high:",high)
#     print("mid:",mid)
#     i+=1
#     if a[mid]==key:
#         print("f1",mid)
#         break

#     elif a[mid]>key:
#         high=mid-1
#         if low>high:
#             print("f2",low)
#             break

#     else:
#         low=mid+1
#         if low>high:
#             print("f3",low)
#             break

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left

print(searchInsert(a,key))