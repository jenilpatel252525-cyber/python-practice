import bisect
from collections import deque

arr = [1, 2, 3, 4, 5]
k = 4
x = 3

p = bisect.bisect_left(arr, x)

# choose closest index
if p < len(arr) and arr[p] == x:
    i = p
elif p == 0:
    i = 0
else:
    i = p - 1

d = deque()
d.append(arr[i])
count = 1

left = i - 1
right = i + 1

while count < k:
    if left >= 0 and right < len(arr):
        if abs(x - arr[left]) <= abs(x - arr[right]):
            d.appendleft(arr[left])
            left -= 1   # FIX: move left pointer left
        else:
            d.append(arr[right])
            right += 1
    elif left >= 0:
        d.appendleft(arr[left])
        left -= 1
    else:
        d.append(arr[right])
        right += 1
    count += 1

print(list(d))
