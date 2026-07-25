# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.traversal = []
    
    #must use BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return self.traversal
      
        queue = []
        queue.append(root)
        self.traversal.append([root.val])
        while queue:
            children = []
            self.traversal.append([])
            while queue:
                node = queue.pop(0)
                if node.left:
                    children.append(node.left)
                    self.traversal[-1].extend([node.left.val])
                if node.right:
                    children.append(node.right)
                    self.traversal[-1].extend([node.right.val])
            queue.extend(children)
        for i in range(len(self.traversal)):
            if len(self.traversal[i]) < 1:
                self.traversal.remove(self.traversal[i])
        return self.traversal   