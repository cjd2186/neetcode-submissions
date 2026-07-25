# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# nodes are unique
#not just binary tree, binary search tree! 

#need to traverse upwards in the tree until they share a node
#only need to return the common ancestor

#return when the both go to the same node, or when

# BFS -->  Left root Right

#Case to check:
#need to check if p and q are in left and right subtrees
class Solution:
    def __init__(self):
        self.lca = -101
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        print(root.val)
        # if p < q, p is in left subtree
        #go left is p and q are less than root
        if max(p.val, q.val) >= root.val and min(p.val, q.val) <= root.val:
            self.lca = root
        if max(p.val, q.val) < root.val:
            print(root.val, "left!")
            self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            print(root.val, "right!")
            self.lowestCommonAncestor(root.right, p, q)   
        return self.lca