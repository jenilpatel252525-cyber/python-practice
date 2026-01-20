a=[2,5,6,0,0,1,2,3]
 
target = 5

def binarysearch(a,low,high):
    if low>high:
        return False
    mid = ( low + high )//2
    
    if a[mid]==target:
        return True
    
    if a[low] == a[mid] == a[high]:
        return binarysearch(a, low + 1, high - 1, target)
    
    if a[low]<=a[mid-1]:
        if a[low]<=target<=a[mid-1]:
            high=mid-1
            return binarysearch(a,low,high)
        else:
            low=mid+1
            return binarysearch(a,low,high)
    else:
        if a[mid+1]<=target<=a[high]:
            low=mid+1
            return binarysearch(a,low,high)
        else:
            high=mid-1
            return binarysearch(a,low,high)
    
print(binarysearch(a,0,len(a)-1))