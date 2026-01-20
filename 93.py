a=[4,6,2,5,7,9,1,3]

def quicksort(a,low,high):
    if low>=high:
        return
    pivot=a[low]
    i=low+1
    j=high
    while i<=j:
        while a[i]<=pivot and a[i] <= pivot:
            i+=1
        while a[j]>pivot and a[j] > pivot:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[low],a[j]=a[j],a[low]
    quicksort(a,low,j-1)
    quicksort(a,j+1,high)
    
quicksort(a,0,len(a)-1)

print(a)