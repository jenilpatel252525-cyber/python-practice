s = "the sky is blue"
chars = list(s)   # convert to list for mutability

i = 0
j = len(chars) - 1

previ = 0
prevj = len(chars) - 1

while i < j:
    # find first word from left
    while i < len(chars) and chars[i] != " ":
        i += 1
    # find first word from right
    while j >= 0 and chars[j] != " ":
        j -= 1

    part1 = s[previ:i]        # first word
    part2 = s[j+1:prevj+1]    # last word

    # swap them inside chars
    # replace first word with spaces, then insert last word
    chars[previ:i] = list(" " * (i - previ))  
    chars[previ:previ+len(part2)] = list(part2)

    # replace last word with spaces, then insert first word
    chars[j+1:prevj+1] = list(" " * (prevj - j))  
    chars[prevj-len(part1)+1:prevj+1] = list(part1)

    # move inward
    previ = i + 1
    prevj = j - 1   # 👈 careful, j points to space
    i = previ
    j = prevj

    print("".join(chars))   # debug progress
    
    
    
    
    
    
    
s = "the sky is blue"
chars = list(s)

# Step 1: Reverse the entire string
chars.reverse()  # now chars = ['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']

n = len(chars)
start = 0

# Step 2: Reverse each word
for end in range(n + 1):
    if end == n or chars[end] == ' ':
        # Reverse word from start to end-1
        i, j = start, end - 1
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        start = end + 1  # move to next word

# Step 3: Convert back to string
reversed_s = "".join(chars)
print(reversed_s)
