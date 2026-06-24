# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        #Divide list into halfs
        #reverse second half and weave into first half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is now at the midpoint
        #init is at the beginning
        
        l2 = slow.next
        slow.next = None
        prev = None
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp
        
        #head now has first list
        #prev has reversed second list

        #merge the two!
        merged = head

        while prev and head:
            hn = head.next
            pn = prev.next

            print(head.val)
            head.next = prev
            prev.next = hn
            print(prev.val)
            
            head = hn
            prev = pn


        return None