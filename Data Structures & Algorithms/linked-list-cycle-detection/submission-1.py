# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        if not head:
            return False
        while head.next:
            if head.val in visited:
                return True
            visited.append(head.val)
            head = head.next
        return False