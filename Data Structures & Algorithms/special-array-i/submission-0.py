class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        while r < len(nums):
            #one must be even, other odd
            left = nums[l]
            right = nums[r]
            if left % 2 == 0 and right % 2 == 0:
                return False
            if left % 2 == 1 and right % 2 == 1:
                return False
            l+=1
            r+=1
        return True