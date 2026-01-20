
a = [2, 0, 2, 1, 1, 0]
low = 0
mid = 0
high = len(a) - 1

while mid <= high:
    if a[mid] == 0:
        a[low], a[mid] = a[mid], a[low]
        low += 1
        mid += 1
    elif a[mid] == 1:
        mid += 1
    else:  # a[mid] == 2
        a[mid], a[high] = a[high], a[mid]
        high -= 1

print(a)  # [0, 0, 1, 1, 2, 2]


a = [2, 1, 0, 2, 1, 0, 2, 1, 0]
low = 0
mid = 0
high = len(a) - 1

i = 0
while i <= high:
    if a[i] == 0:
        a[i], a[low] = a[low], a[i]
        if i == low:
            i += 1  # move forward only if i was the same as low
        low += 1
        mid += 1  # 0s are before mid
    elif a[i] == 1:
        i += 1
        mid += 1
    else:  # a[i] == 2
        a[i], a[high] = a[high], a[i]
        high -= 1
        # do NOT increment i here, because the new value at i must be checked again

print(a)
