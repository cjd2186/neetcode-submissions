# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS, keep max of all children
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.traverse_sub(root.left)
        if root.right:
            right_depth = self.traverse_sub(root.right)
        
        return max(left_depth, right_depth) + 1

    def traverse_sub(self, root) -> int:
        if not root:
            return 0
        left_depth = self.traverse_sub(root.left)
        right_depth = self.traverse_sub(root.right)
        return max(left_depth + 1, right_depth + 1)