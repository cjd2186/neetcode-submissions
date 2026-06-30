# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS -- use a queue, iterative
# root in the queue
# replace root with children
# track level, keep going until queue is empty
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        level = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue[0]
                queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level +=1
        return level