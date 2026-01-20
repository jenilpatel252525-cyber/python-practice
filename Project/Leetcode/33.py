a=[1, 3, 2, 2, 5,4,4,4,4,5,5,4, 2, 3, 7]

i=0
l=0
length=0
max=-1
min=100
flag=True

while i<len(a):
    if a[i]>max:
        max=a[i]
        # print(max)
    if a[i]<min:
        min=a[i]
        # print(min)
    if max-min==1:
        if l==0:
            l+=2
        else:
            l+=1
        i+=1
        flag=False
    else:
        if l>length:
            length=l
        l=0
        max=a[i]
        min=a[i]
        if flag:
            i+=1
        else:
            flag=True
        

print(length)





from collections import Counter

def longestHarmonious(nums):
    # Count the frequency of each number in the array
    freq = Counter(nums)
    
    max_length = 0
    
    # Iterate through the unique numbers in the array
    for num in freq:
        # Check if num+1 exists in the frequency map
        if num + 1 in freq:
            # Calculate the length of the subsequence
            max_length = max(max_length, freq[num] + freq[num + 1])
    
    return max_length

# Test cases
print(longestHarmonious([1, 3, 2, 2, 5, 2, 3, 7]))  # Output: 5
print(longestHarmonious([1, 2, 3, 4]))              # Output: 2
print(longestHarmonious([1, 1, 1, 1]))              # Output: 0
