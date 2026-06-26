# O(1) extra space
# O(n) time

# Modift existing array --> mark seen values as negative 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupe = -1
        for i in range(0, len(nums)):
            if nums[abs(nums[i])-1] < 0:
                dupe = abs(nums[i])
                break
            else:
                # Mark this index as seen
                nums[abs(nums[i])-1] *= -1
        return dupe