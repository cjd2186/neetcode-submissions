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
            print(level)
            for node in level:
                print("root", node.val)
                if node.left:
                    print("left", node.left.val)
                    level_nodes.append(node.left)
                if node.right:
                    print("right", node.right.val)
                    level_nodes.append(node.right)
            queue.append(level_nodes)
            i+=1
            [print(len(node)) for node in queue]
            if i == 100:
                return output
            if len(level_nodes)>0:
                output.append(level_nodes[-1].val)
        return output