from collections import Counter, defaultdict

def isPossible(nums):
    freq = Counter(nums)       # Count of each number
    end_map = defaultdict(int) # Subsequences ending at a number

    for num in nums:
        if freq[num] == 0:
            continue
        
        freq[num] -= 1
        
        # Try to extend a subsequence ending with num-1
        if end_map[num-1] > 0:
            end_map[num-1] -= 1
            end_map[num] += 1
        # Try to create a new subsequence num, num+1, num+2
        elif freq[num+1] > 0 and freq[num+2] > 0:
            freq[num+1] -= 1
            freq[num+2] -= 1
            end_map[num+2] += 1
        else:
            return False
    
    return True







def isPossible(nums):
    subseqs = []  # each subsequence is [elements] or (last_element, length)
    
    for num in nums:
        # Find subsequences that can take num
        candidates = [seq for seq in subseqs if seq[-1] == num - 1]
        
        if candidates:
            # Prefer one whose length < 3, else take any
            chosen = None
            for seq in candidates:
                if len(seq) < 3:
                    chosen = seq
                    break
            if not chosen:
                chosen = candidates[0]
            chosen.append(num)
        else:
            subseqs.append([num])
    
    # Check all subsequences have length >= 3
    return all(len(seq) >= 3 for seq in subseqs)