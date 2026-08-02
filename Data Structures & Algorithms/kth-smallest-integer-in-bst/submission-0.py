# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BST tree -- left and right mean to go smaller or larger
#naive approach is just get all of the items and put them into a sorted array

#when you get to a leaf, there are at least Height number of elements larger than items
#left subtree has at least 1 node less than root
#right subtree has at least 1 node greater than root

#keep going left until you hit leaf, then start adding counter until you hit k
#unraveling of the DFS will go from lowest to highest -- just stop at K
class Solution:
    def __init__(self):
        #TODO: maybe forgo counter and instead decrement k?
        self.counter = 1
        self.output = -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.output

    def traverse(self, root, k):
        if not root:
            return 
        if root.left:
            self.traverse(root.left, k)
        print("val: ", root.val)
        print("counter: ", self.counter)
        if self.counter == k:
            self.output = root.val
        self.counter += 1
        if root.right:
            self.traverse(root.right, k)
        return