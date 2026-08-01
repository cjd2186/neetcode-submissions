# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS approach
# all left children must be less than root
# all right children must be greater than root
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        minMax = [-1001, 1001]
        return self.traverseTree(root, minMax)

    #want each path to have its own isValid
    def traverseTree(self, root: Optional[TreeNode], minMax: list[int]):
        if not root:
            return True
        if not root.val < minMax[1] or not root.val > minMax[0]:
            return False
        return self.traverseTree(root.left,  [minMax[0], root.val]) and self.traverseTree(root.right, [root.val, minMax[1]])
        