a=[1,2,3,4,5,6,7]

k=6
j=0

for i in range(k,len(a)):
    a[j],a[i]=a[i],a[j]
    j+=1

p=0
q=len(a)-k-1

if k<=int(len(a)/2):
    while p<k:
        a[p],a[q]=a[q],a[p]
        p+=1
        q-=1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

quick_sort(a,0,k-1)
quick_sort(a,k,len(a)-1)

print(a)










def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse full array
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)

    # Step 3: Reverse remaining n-k elements
    reverse(k, n - 1)