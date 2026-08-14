#Naive is to check if each item is in the array again, but no extra space
#Counter --> counter frequency of each item, if any is greater than 1 return True
#Time: O(n) counter takes 1 pass through list
#Space: O(n) create counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        count = Counter(nums)
        if max(count.values()) > 1:
            return True
        return False