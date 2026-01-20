a=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 3
flag=True

low1=0
high1=len(a)-1

while low1<=high1:
    mid1=int((low1+high1)/2)
    low2=0
    high2=len(a[0])-1
    while low2<=high2:
        if a[mid1][0]<=target<=a[mid1][len(a[0])-1]:
            mid2=int((low2+high2)/2)
            if a[mid1][mid2]==target:
                print("true")
                flag=False
                exit()
            elif a[mid1][mid2]>target:
                high2=mid2-1
            else:
                low2=mid2+1
        elif target>a[mid1][len(a[0])-1]:
            low1=mid1+1
        else:
            high1=mid1-1
            
if flag:
    print(False)
    
    
    
    
    
a = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

m = len(a)
n = len(a[0])

low = 0
high = m * n - 1

while low <= high:
    mid = (low + high) // 2
    row = mid // n
    col = mid % n
    mid_val = a[row][col]

    if mid_val == target:
        print("true")
        break
    elif mid_val < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("false")  # runs only if loop ends without break
