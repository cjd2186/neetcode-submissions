# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#each level should only have 1 value
#if a level has multiple values, return the right value
#BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        queue = []
        queue.append([root])
        output.append(root.val)
        i=0
        while queue:
            level = queue.pop()
            level_nodes = []
            for node in level:
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            queue.append(level_nodes)
            i+=1
            if i == 100:
                return output
            if len(level_nodes)>0:
                output.append(level_nodes[-1].val)
        return output