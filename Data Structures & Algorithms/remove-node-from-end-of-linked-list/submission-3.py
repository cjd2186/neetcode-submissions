# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse list first
        rev = None
        while head:
            tmp = head.next
            head.next = rev
            rev = head
            head = tmp 
        

        dummy = rev
        prev = ListNode(0, rev)
        #for i in range (1, n):
        i=1
        while rev:
            if i == n:
                prev.next = rev.next
                break
            prev = rev
            rev = rev.next
            i+=1
            
        corr = None
        if n == 1:
            output = dummy.next
        else:
            output = dummy
        while output:
            tmp = output.next
            output.next = corr
            corr = output
            output = tmp 
        return corr