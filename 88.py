a = [1, 2, 3]
b = []  # this will store all subsets

def subsets(i, current):
    if i == len(a):
        b.append(current[:])  # add a copy of current subset
        return
    
    current.append(a[i])         # Line A: Include a[i]
    subsets(i + 1, current)      # Line B: Recurse with inclusion

    current.pop()                # Line C: Backtrack (remove a[i])
    subsets(i + 1, current)      # Line D: Recurse with exclusion

# Call the function starting from index 0 with empty subset
subsets(0, [])

print(b)



a = [1, 2, 3]
b = []

def subsets(i, current):
    # Append subset first (before exploring further)
    b.append(current[:])
    
    for j in range(i, len(a)):
        current.append(a[j])          # choose
        subsets(j + 1, current)       # explore
        current.pop()                 # un-choose (backtrack)

subsets(0, [])
print(b)