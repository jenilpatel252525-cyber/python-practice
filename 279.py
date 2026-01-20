chars=["a","a","a","b","c","c","c","c","c","d","d","e","f","f","f","f","f","f","f","f","f","f","g"]

i = 0
while i < len(chars):
    curr = chars[i]
    count = 1
    j = i + 1
    while j < len(chars) and chars[j] == curr:
        count += 1
        j += 1
    if count > 1:
        del chars[i+1:j]
        for digit in str(count):   # handle multi-digit counts
            chars.insert(i+1, digit)
            i += 1
    i += 1

print(chars)