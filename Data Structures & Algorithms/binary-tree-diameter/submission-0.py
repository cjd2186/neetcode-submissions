# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findHeight(root)
        return self.diameter
    
    def findHeight(self, root):
        if not root:
            return 0
        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)
        d =  leftHeight + rightHeight
        self.diameter = max(d, self.diameter)
        return 1 + max(leftHeight, rightHeight)