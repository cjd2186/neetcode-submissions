class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            #use last bit to determine if odd/even --> bit mask
            if nums[i-1] & 1 == nums[i] & 1:
                return False
        return True