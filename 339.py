from collections import Counter

s = "cbacdcbc"
count = Counter(s)

stack = []
visited = set()

for c in s:
    count[c] -= 1

    if c in visited:
        continue

    while stack and c < stack[-1] and count[stack[-1]] > 0:
        visited.remove(stack.pop())

    stack.append(c)
    visited.add(c)

print("".join(stack))  # acdb