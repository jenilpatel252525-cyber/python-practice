a=[10,20,30,40,1,2,3,4]

j=len(a)//2

for i in range(j):
    if a[i]>a[j]:
        a[i],a[j]=a[j],a[i]
        k=j
        while j<len(a)-1:
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                j+=1
            else:
                break
        j=k
            
print(a)






import math

def merge_in_place_gap(arr):
    n = len(arr)
    
    def next_gap(g):
        if g <= 1:
            return 0
        return (g + 1) // 2  # ceiling division

    gap = next_gap(n)

    while gap > 0:
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            i += 1
        gap = next_gap(gap)

# Example usage
a = [10, 20, 30, 40, 1, 2, 3, 4]
merge_in_place_gap(a)
print(a)  # Output: [1, 2, 3, 4, 10, 20, 30, 40]