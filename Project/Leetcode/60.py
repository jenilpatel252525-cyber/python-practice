from collections import defaultdict

def count_xor_less_equal_k(a, K):
    count = 0
    prefix_xor = 0
    freq = defaultdict(int)
    freq[0] = 1  # To include subarrays starting from index 0

    for num in a:
        prefix_xor ^= num
        for p in freq:
            if (prefix_xor ^ p) <= K:
                count += freq[p]
        freq[prefix_xor] += 1

    return count

def count_subarrays_with_xor_in_range(a, L, R):
    return count_xor_less_equal_k(a, R) - count_xor_less_equal_k(a, L - 1)

# Example usage
a = [2, 3, 1, 6, 7]
L = 2
R = 6

print(count_subarrays_with_xor_in_range(a, L, R))  # Output: 7
