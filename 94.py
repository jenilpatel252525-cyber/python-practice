a = [10, 1, 2, 7, 6, 1, 5]
target = 8
b = []
curr = []

a.sort()  # Sort to handle duplicates

def combination(i):
    if sum(curr) == target:
        b.append(curr[:])
        return
    if sum(curr) > target:
        return

    for j in range(i, len(a)):
        if j > i and a[j] == a[j - 1]:  # Skip duplicates
            continue
        curr.append(a[j])
        combination(j + 1)  # Move to next index
        curr.pop()

combination(0)
print(b)
