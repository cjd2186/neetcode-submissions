# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#root left right ---
#BFS and add them as parts of string
#use N as none
# use | as a deliminter if the numbers are more than a single digit
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoding = ""
        if not root:
            return encoding
        queue = []
        queue.append([root])
        encoding += "|"
        encoding += str(root.val)
        while queue:
            level = queue.pop()
            level_nodes = []
            level_encoding = ""
            allN=True
            for node in level:
                if node.left:
                    level_nodes.append(node.left)
                    level_encoding += "|"
                    level_encoding += str(node.left.val)
                    level_encoding += "|"
                    allN=False
                else:
                    level_encoding += "|"
                    level_encoding += "N"
                    level_encoding += "|"
                if node.right:
                    level_nodes.append(node.right)
                    level_encoding += "|"
                    level_encoding += str(node.right.val)
                    level_encoding += "|"
                    allN=False
                else:
                    level_encoding += "|"
                    level_encoding += "N"
                    level_encoding += "|"
            if len(level_nodes) > 0:
                queue.append(level_nodes)
            if not allN:
                encoding += level_encoding
            
        return encoding

        
    # Decodes your encoded data to tree.
    #root left right -- two after become kids
    # use a queue to track the root -- same idea as BFS encoding
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) < 1:
            return
        encoding = data.split("|")
        encode = []
        for i in range(len(encoding)):
            if encoding[i] != "":
                encode.append(encoding[i])

        root = TreeNode(int(encode[0]))
        og_root= root
        root_queue = [root]
        for i in range(2, len(encode), 2):
            root = root_queue.pop()
            if encode[i-1] != "N":
                root.left = TreeNode(int(encode[i-1]))
                root_queue.insert(0, root.left)
            if encode[i] != "N":
                root.right = TreeNode(int(encode[i]))
                root_queue.insert(0, root.right)

        return og_root