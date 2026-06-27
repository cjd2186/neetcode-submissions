# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach
# make list 1 and list 2 into concatenated numbers, add them, reverse, put into new list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        while l1:
            num1.insert(0, str(l1.val))
            l1=l1.next
        num2 = []
        while l2:
            num2.insert(0, str(l2.val))
            l2=l2.next
        
        string1 = ''.join(num1)
        string2 = ''.join(num2)

        values = int(string1) + int(string2)
        values_list = list(str(values))[::-1]
        
        
        new_list = ListNode(values_list[0])
        output = new_list
        for i in range(0, len(values_list)-1):
            new_list.next = ListNode(values_list[i+1])
            new_list = new_list.next
        return output