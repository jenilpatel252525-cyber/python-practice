def countArrangement(n):
    used = [False] * (n + 1)
    
    def backtrack(pos):
        if pos > n:
            return 1  # found valid arrangement
        total = 0
        for num in range(1, n + 1):
            if not used[num] and (num % pos == 0 or pos % num == 0):
                used[num] = True
                total += backtrack(pos + 1)
                used[num] = False
        return total
    
    return backtrack(1)
