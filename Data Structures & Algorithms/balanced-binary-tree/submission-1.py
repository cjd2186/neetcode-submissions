# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.height = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.findHeight(root)
        return self.height

    #find height of the tree recursively
    def findHeight(self, root):
        if not root or not self.height:
            return 0
        leftHeight = self.findHeight(root.left)
        rightHeight = self.findHeight(root.right)
        # if height diffference is great than 1, set bool to False
        if abs(leftHeight - rightHeight) > 1:
            self.height = False 
        elif abs(leftHeight - rightHeight) > 1 and self.height:
            self.height = True
        return max(leftHeight, rightHeight) + 1