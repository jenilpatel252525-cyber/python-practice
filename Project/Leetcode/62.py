def longest_subarray_xor_less_than_k(a, K):
    n = len(a)
    prefix_xor = [0] * (n + 1)
    
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ a[i]
    
    max_len = 0

    # Check all subarrays
    for i in range(n):
        for j in range(i + 1, n + 1):
            xor_val = prefix_xor[j] ^ prefix_xor[i]
            if xor_val < K:
                max_len = max(max_len, j - i)
    
    return max_len

# Example:
a = [8, 1, 2, 12]
K = 10
print(longest_subarray_xor_less_than_k(a, K))  # Output: 2 ([1,2])
