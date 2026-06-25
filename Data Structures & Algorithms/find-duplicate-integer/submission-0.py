class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = []
        for i in range(0, len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.append(nums[i])