nums1 = [0,0,0,0]
nums2 = [0,0,0,0]
nums3 = [0,0,0,0]
nums4 = [0,0,0,0]

s1={}
s2={}
s3={}
s4={}

def find4(curr):
    if curr in s4:
        return s4[curr]
    temp=0
    for i in nums4:
        if curr+i==0:
            temp+=1
    s4[curr]=temp
    return temp
            
def find3(curr):
    if curr in s3:
        return s3[curr]
    temp=0
    for i in nums3:
        temp+=find4(curr+i)
    s3[curr]=temp
    return temp

def find2(curr):
    if curr in s2:
        return s2[curr]
    temp=0
    for i in nums2:
        temp+=find3(curr+i)
    s2[curr]=temp
    return temp

path=0

for i in nums1:
    if i in s1:
        path+=s1[i]
        continue
    path+=find2(i)
    s1[i]=find2(i)
    
print(path)








from collections import defaultdict

def fourSumCount(nums1, nums2, nums3, nums4):
    count = 0
    hashmap = defaultdict(int)

    # Store all possible sums of nums1 + nums2
    for a in nums1:
        for b in nums2:
            hashmap[a + b] += 1

    # For each possible nums3 + nums4, check if the negated sum exists
    for c in nums3:
        for d in nums4:
            count += hashmap[-(c + d)]

    return count

# Example usage
nums1 = [0]
nums2 = [0, 0]
nums3 = [0, 0, 0]
nums4 = [0, 0, 0, 0]

print(fourSumCount(nums1, nums2, nums3, nums4))  