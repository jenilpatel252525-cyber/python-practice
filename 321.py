s = "leet2code3"

k = 10

temp=""

i=0

while len(temp)<k:
    c=""
    if s[i].isdigit():
        c+=int(s[i])*temp
        temp=c
    else:
        temp+=s[i]
    i+=1
    
print(temp[k-1])







s = "leet2code3"
k = 10

# Step 1: find total decoded length (instead of building string)
length = 0
i = 0

while length < k:
    if s[i].isdigit():
        length *= int(s[i])
    else:
        length += 1
    i += 1

# Step 2: walk backwards to find kth character
i -= 1

while i >= 0:
    if s[i].isdigit():
        length //= int(s[i])
        k %= length
    else:
        if k == 0 or k == length:
            print(s[i])
            break
        length -= 1
    i -= 1
