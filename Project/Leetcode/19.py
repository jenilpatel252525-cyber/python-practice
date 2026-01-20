from collections import Counter

def intersect(nums1, nums2):
    count = Counter(nums1)
    result = []

    for num in nums2:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result


a=[1,2,2,3,4,5]

b=[2,2,3,3,5]

c=[]

i=0
j=0

while i<len(a) and j<len(b):
    if a[i]==b[j]:
        c.append(a[i])
        i+=1
        j+=1
    elif a[i] < b[j]:
        i+=1
    else:
        j+=1

print(c)