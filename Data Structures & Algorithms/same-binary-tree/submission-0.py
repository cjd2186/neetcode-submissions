# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Traverse each tree then compare stored arrays ==> O(N) space
class Solution:
    def __init__(self):
        self.p_arr = []
        self.q_arr = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.traverseTree('p', p)
        self.traverseTree('q', q)
        if len(self.p_arr) != len(self.q_arr):
            return False
        for i in range(len(self.p_arr)):
            if self.p_arr[i] != self.q_arr[i]:
                return False
        return True

    def traverseTree(self, mode: str, root: Optional[TreeNode]):
        if not root:
            if mode == 'p':    
                self.p_arr.append('None')
            elif mode == 'q':    
                self.q_arr.append('None')
            return
        if mode == 'p':
            self.p_arr.append(root.val)
            self.traverseTree('p', root.left)
            self.traverseTree('p', root.right)
        elif mode =='q':
            self.q_arr.append(root.val)
            self.traverseTree('q', root.left) 
            self.traverseTree('q', root.right)
        return