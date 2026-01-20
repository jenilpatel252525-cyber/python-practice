def isValidSerialization(preorder: str) -> bool:
    nodes = preorder.split(",")
    slots = 1   # root has 1 slot

    for node in nodes:
        slots -= 1  # occupy a slot
        if slots < 0:
            return False
        if node != "#":
            slots += 2  # non-null node creates 2 new slots
    return slots == 0








def isValidSerialization(preorder: str) -> bool:
    nodes = preorder.split(",")
    if not nodes:
        return False

    if nodes[0] == "#":
        return len(nodes) == 1

    s = {i: [False, False] for i in nodes if i != "#"}  # child slots
    stack = [nodes[0]]

    for i in range(1, len(nodes)):
        if not stack:
            return False

        curr = stack[-1]

        # assign current node to the first available child slot
        if not s[curr][0]:
            s[curr][0] = True
        elif not s[curr][1]:
            s[curr][1] = True

        # if parent now has both children, pop it
        while stack and s[stack[-1]][0] and s[stack[-1]][1]:
            stack.pop()

        # push current node if it is not null
        if nodes[i] != "#":
            stack.append(nodes[i])

    # stack should be empty if all nodes processed correctly
    return not stack



print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))  # True
print(isValidSerialization("1,#"))                        # False
print(isValidSerialization("9,#,#,1"))                    # False
print(isValidSerialization("#"))                          # True
print(isValidSerialization("9,#,#"))                      # True
