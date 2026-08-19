class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #left to right
        #if 0, remove, and append
        for i, num in enumerate(nums):
            if num == 0:
                nums.remove(0)
                nums.append(0)