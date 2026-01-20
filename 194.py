strs = ["abaxxc","cdyzc","eapbe"]

checked=set()

ans=""
idx=None

def ischecked(i,j):
    if j in checked:
        return True
    checked.add(j)
    for k in range(i+1,len(strs)):
        if j in strs[k]:
            return True
    return False

for i in range(len(strs)):
    temp=""
    for j in strs[i]:
        if ischecked(i,j):
            continue
        else:
            temp+=j
    if len(temp)>len(ans):
        ans=temp
        idx=i
        
final=""
        
for i in strs[idx]:
    if i in ans:
        final+=i
        
print(final)



strs = ["abaxxc", "cdyzc", "eapbe","rrrrrrr"]

# Precompute set of characters for each string
char_sets = [set(s) for s in strs]

checked = set()
ans = ""
idx = None

curr=[]

def ischecked(i, j):
    if j in checked:  # already processed char
        return True
    # Check if char exists in any future string
    for k in range(i+1, len(strs)):
        if j in char_sets[k]:  # O(1) lookup
            checked.add(j)
            return True
    return False

# Main loop
for i in range(len(strs)):
    temp = ""
    for j in strs[i]:
        if ischecked(i, j):
            continue
        else:
            checked.add(j)
            temp += j
    curr.append(temp)
    
char_sets2 = [set(s) for s in curr]
    
for i in range(len(strs)):
    temp=""
    for j in strs[i]:
        if j in char_sets2[i]:
            temp+=j
    if len(temp)>len(ans):
        ans=temp

# Build final string

print(ans)




strs = ["abaxxc", "cdyzc", "eapbe"]

# Precompute set of characters for each string
char_sets = [set(s) for s in strs]

# Precompute union of characters for all future strings
future_sets = [set() for _ in range(len(strs))]
future_union = set()
for i in range(len(strs)-1, -1, -1):   # go backwards
    future_sets[i] = future_union.copy()
    future_union |= char_sets[i]

checked = set()
ans = ""
curr = []

def ischecked(i, j):
    if j in checked:
        return True
    if j in future_sets[i]:  # O(1) lookup
        checked.add(j)
        return True
    return False

# First pass
for i in range(len(strs)):
    temp = ""
    for j in strs[i]:
        if ischecked(i, j):
            continue
        checked.add(j)
        temp += j
    curr.append(temp)

# Second pass
char_sets2 = [set(s) for s in curr]
for i in range(len(strs)):
    temp = ""
    for j in strs[i]:
        if j in char_sets2[i]:
            temp += j
    if len(temp) > len(ans):
        ans = temp

print(ans)
print(future_sets)