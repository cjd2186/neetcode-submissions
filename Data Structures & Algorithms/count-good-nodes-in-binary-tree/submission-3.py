# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS on each node, on the way down, see if node is greater than max, if so it is a good node
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.pathMax = -101
        return self.findGood(root, self.pathMax)

    def findGood(self, root:TreeNode, pathMax: int) -> int:
        if not root:
            return self.good
        #reset pathMax, since we are at the end of the current path
        #only reset pathMax if the node is not a leaf node (i.e. has a child)
        if root.val >= pathMax:
            self.good+=1
            if root.left or root.right:
                pathMax = root.val
        if root.left:
            self.findGood(root.left, pathMax)
        if root.right:
            self.findGood(root.right, pathMax)
        return self.good