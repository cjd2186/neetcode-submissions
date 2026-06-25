# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach
# Take list, find length, remove correct node
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #find length
        length = 0
        lnode = head
        while lnode:
            length +=1
            lnode = lnode.next

        #remove node at length - n
        remove_idx = length - n
        prev = ListNode(0, None)
        output = ListNode(0, head)
        i = 0
        while head and i <= remove_idx:
            if i == remove_idx:
                prev.next = head.next      
                if i == 0:
                    output = output.next
            else:
                prev = head
            head = head.next
            i+=1
        return output.next