def findRepeatedDnaSequences(s: str):
    seen = set()
    repeated = set()
    
    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)
    
    return list(repeated)


# Example usage
print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
# Output: ["AAAAAAAAAA"]








def findRepeatedDnaSequences(s: str):
    if len(s) < 10:
        return []
    
    seen = {}       # key = (first_char, last_char), value = list of start indices
    repeated = set()
    
    for i in range(len(s) - 9):
        substring = s[i:i+10]
        key = (substring[0], substring[-1])
        
        if key in seen:
            # Compare with candidates having same first & last chars
            for start in seen[key]:
                if s[start:start+10] == substring:
                    repeated.add(substring)
                    break
            seen[key].append(i)
        else:
            seen[key] = [i]
    
    return list(repeated)


# Example usage
print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
# Output: ["AAAAAAAAAA"]