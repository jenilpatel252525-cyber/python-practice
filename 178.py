nums = [4,14,2]

def count_ones(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

count=0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        k=nums[i]^nums[j]
        count+=count_ones(k)
        
print(count)






def totalHammingDistance(nums):
    total = 0
    n = len(nums)
    
    for i in range(32):  # For 32-bit integers
        bit_count = 0
        for num in nums:
            bit_count += (num >> i) & 1  # Count of 1s at bit i
        
        total += bit_count * (n - bit_count)  # Ones * Zeros
        
    return total