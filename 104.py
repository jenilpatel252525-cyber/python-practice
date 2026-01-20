preorder = [1, 2, 4, 8, 11, 9, 5, 3, 6, 10, 7]

inorder = [11, 8, 4, 9, 2, 5, 1, 6, 10, 3, 7]

tree = [preorder[0]]

i=0

def findleft(curr):
    i=preorder.index(curr)
    if i<len(preorder)-1:
        left=preorder[i+1]
    else:
        return None
    j=inorder.index(curr)
    k=inorder.index(left)
    if k<j:
        return left
    else:
        return None
    
# def findleft(curr):
#     # Index of current node in inorder
#     in_index = inorder.index(curr)

#     # If there's no node before curr in inorder, no left child
#     if in_index == 0:
#         return None

#     # Candidates for left subtree = all nodes before curr in inorder
#     left_candidate = inorder[:in_index]

#     # From preorder, return the first node that is in the left subtree
#     for node in preorder:
#         if node in left_candidate:
#             return node

#     return None

    
def findright(curr):
    # Find the index of current node in inorder traversal
    in_index = inorder.index(curr)

    # If there's no element after curr in inorder, no right child
    if in_index == len(inorder) - 1:
        return None

    # The right child in a binary tree appears after the current node in inorder,
    # and it must be found in the preorder traversal (after curr)
    # So we check for the next inorder node that comes after curr
    right_candidate = inorder[in_index + 1:]

    # From preorder, find which of these right candidates appears first
    for node in preorder:
        if node in right_candidate:
            return node

    return None

tree = {}
visited = set()

def build(curr):
    if curr in visited:
        return
    visited.add(curr)

    left = findleft(curr)
    right = findright(curr)

    tree[curr] = {
        "left": left,
        "right": right
    }

    if left: build(left)
    if right: build(right)

build(preorder[0])
root = preorder[0]

# Level-order traversal with None for missing children
def level_order_array(root, tree):
    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node is None:
            result.append(None)
            continue

        result.append(node)

        # Add children (even if None)
        left = tree.get(node, {}).get("left")
        right = tree.get(node, {}).get("right")

        queue.append(left)
        queue.append(right)

    # Remove trailing None values for LeetCode-style output
    while result and result[-1] is None:
        result.pop()

    return result

# ✅ Final Output
output = level_order_array(root, tree)
print(output)