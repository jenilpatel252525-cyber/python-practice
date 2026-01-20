a=[4,6,7,0,0]

b=[5,8]

# i=len(a)-len(b)-1

# j=b.pop()

# k=False

# l=True

# n=len(b)

# while i >=0:
#     if k==True:
#         if n==0:
#             break
#         n=n-1
#         j=b.pop()
#         k=False
#         l=True
#     if j >= a[i]:
#         print(i)
#         a.insert(i+1,j)
#         print("yes")
#         a.pop()
#         k=True
#         print(k)
#         l=False
#     if l==True:
#         i=i-1

# print(a)

def merge(nums1, m, nums2, n):
    # Start from the end of the actual data in nums1 and nums2
    i = m - 1  # Last element in nums1 (not including the trailing 0s)
    j = n - 1  # Last element in nums2
    k = m + n - 1  # Last index in nums1

    # Merge in reverse to avoid overwriting nums1's data
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are any leftover elements in nums2 (not nums1, because it's already in place)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

merge(a,3,b,2)

print(a)