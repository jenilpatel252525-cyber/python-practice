def removeDuplicateLetters(s: str) -> str:
    last_index = {ch: i for i, ch in enumerate(s)}  # last occurrence of each char
    stack = []
    in_stack = set()

    for i, ch in enumerate(s):
        # skip if already in result
        if ch in in_stack:
            continue

        # maintain lexicographic order
        while stack and ch < stack[-1] and i < last_index[stack[-1]]:
            removed = stack.pop()
            in_stack.remove(removed)

        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)