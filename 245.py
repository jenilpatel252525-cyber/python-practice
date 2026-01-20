def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    # Mapping as a dictionary
    mapping = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }
    
    res = []
    
    def backtrack(index, path):
        if index == len(digits):
            res.append("".join(path))
            return
        for char in mapping[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()  # backtrack
    
    backtrack(0, [])
    return res

# Example usage:
print(letterCombinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']