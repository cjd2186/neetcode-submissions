"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Approach
# Iterate through list first time, making new node for each next in a dict
# Go back through list and connect random pointers each time by finding the correct map
# Keys: first LL; Values: deepcopy

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':       
        if not head:
            return
        og_copy = {}
        while head:
            og_copy[head] = Node(0)
            head = head.next
        
        ogs=list(og_copy.keys())
        copies=list(og_copy.values())
        # og | deep copy
        # want values.val to equal keys.val
        # set up the pointers incrementally too
        
        # for random --> you can access the random node!!
        # .random maps to a node, you say that the random pointer is 
        #.  at the same level as where the random key points to
        deepcopy = og_copy[ogs[0]]
        for j in range(0, len(og_copy)):
            og_copy[ogs[j]].val = ogs[j].val
            if j == len(og_copy) - 1:
                og_copy[ogs[j]].next = None
            else:
                og_copy[ogs[j]].next = og_copy[ogs[j+1]]
            if ogs[j].random:
                og_copy[ogs[j]].random = og_copy[ogs[j].random]
            else:
                og_copy[ogs[j]].random = None
        return deepcopy

    # 3 v n r | 3 v n 
    # 4 v n r | 4 v n
        