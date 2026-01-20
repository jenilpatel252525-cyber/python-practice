inorder = [16, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15, 17]

postorder = [16, 8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 17, 15, 7, 3, 1]

# def findright(curr):
#     i=postorder.index(curr)
#     if i>0:
#         right=postorder[i-1]
#     else:
#         return None
#     j=inorder.index(curr)
#     k=inorder.index(right)
#     if k>j:
#         return right
#     else:
#         return None

def findright(curr):
    in_index = inorder.index(curr)
    if in_index == len(inorder) - 1:
        return None
    right_candidate = inorder[in_index + 1:]
    right = None
    j = postorder.index(curr)
    for i in range(j):
        if postorder[i] in right_candidate:
            right = postorder[i]
    return right
    
def findleft(curr):
    in_index = inorder.index(curr)
    if in_index == 0:
        return None
    left_candidate = inorder[:in_index]
    left=None
    j=postorder.index(curr)
    for i in range(j):
        if postorder[i] in left_candidate:
            left=postorder[i]
    return left