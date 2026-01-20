# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        # Base case: empty array -> no node
        if not nums:
            return None

        # Find max value and its index
        max_val = max(nums)
        max_index = nums.index(max_val)

        # Root is max value
        root = TreeNode(max_val)

        # Recursively build left subtree
        root.left = self.constructMaximumBinaryTree(nums[:max_index])

        # Recursively build right subtree
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])

        return root
