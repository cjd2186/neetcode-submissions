# O(1) extra space
# O(n) time

# Treat list as a linkedlist --> each index points to next index using value
# if linked list is cycle --> val is duplicated

#Floyd's Algorithm
# slow and fast start at head
# slow and fast advance until they meet --> shows that their is a cycle
# reset slow, have fast and slow advance until they meet --> meet at the start of the cycle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #have pointer
        slow = 0
        fast = 0
        while 1:
            slow = nums[slow]
            #advance fast twice --> fast1= nums[fast] nums[fast1] -- nums[nums[fast]]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

"""
i [0, 1, 2, 3]
n [1, 2, 3, 3]
nums[s]: 1
nums[f]: 1
nums[1]: 2

i [0, 1, 2, 3]
n [1, 2, 3, 3]
nums[1]: 2
nums[2]: 3
nums[3]: 3

i [0, 1, 2, 3]
n [1, 2, 3, 3]
nums[2]: 3
nums[3]: 3
nums[3]: 4
"""

"""
i [0, 1, 2, 3, 4]
n [1, 2, 3, 2, 2]
nums[s]: 1
nums[f]: 1
nums[1]: 2

i [0, 1, 2, 3]
n [1, 2, 3, 3]
nums[1]: 2
nums[2]: 3
nums[3]: 3

i [0, 1, 2, 3]
n [1, 2, 3, 3]
nums[2]: 3
nums[3]: 3
nums[3]: 4
"""