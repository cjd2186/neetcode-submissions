# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#space
# height --> O(log(n)) balanced tree
# height --> O(n) non balanced tree
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
        #Diameter is the longest path bet two nodes -- think the width of the subtrees
        # because it doesnt necessarily go through the root, we add the heights and store the diameters
        # if it had to go through the root, we would lose the intermidiate values
        d =  leftHeight + rightHeight
        self.diameter = max(d, self.diameter)
        # add one for height of the current one
        return 1 + max(leftHeight, rightHeight)