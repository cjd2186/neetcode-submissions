# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Traverse main tree until subRoot is reached
# then check if this subtree is identical to the root's tree
class Solution:   
    def __init__(self):
        self.subTravserse = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        #in root, search if left has the subtree or if right has the subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    #is subroot somewhere in the root tree? 
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        print(root.val, subRoot.val)
        if root.val == subRoot.val:            
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False
