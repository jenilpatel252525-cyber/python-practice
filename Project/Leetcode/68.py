# a=[5,7,7,8,8,10]

# target = 8

# start=-1
# end=-1

# i=0 
# j=len(a)-1

# while i<=j:
#     mid=int ((i+j)/2)
#     if a[mid]==target:
#         start=mid
#         end=mid
#         while a[start]==a[start-1] and start>0:
#             start=start-1
#         while a[end]==a[end+1] and end<len(a)-1:
#             end=end+1
#         break
            
# print(start,end)

a = [5, 7, 7, 8, 8, 10]
target = 8

# Function to find first occurrence
def find_first(a, target):
    i, j = 0, len(a) - 1
    res = -1
    while i <= j:
        mid = (i + j) // 2
        if a[mid] == target:
            res = mid
            j = mid - 1  # keep searching on left side
        elif a[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return res

# Function to find last occurrence
def find_last(a, target):
    i, j = 0, len(a) - 1
    res = -1
    while i <= j:
        mid = (i + j) // 2
        if a[mid] == target:
            res = mid
            i = mid + 1  # keep searching on right side
        elif a[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return res

start = find_first(a, target)
end = find_last(a, target)

print(start, end)
