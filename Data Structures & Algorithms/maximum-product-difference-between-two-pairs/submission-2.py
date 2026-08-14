#want to find 2 max ints and 2 min ints --> 4 passes
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = -1
        max2 = -1
        min1 = 100001
        min2 = 100002

        for num in nums:
            max1 = max(max1, num)
            min1 = min(min1, num)
        nums.remove(max1)
        nums.remove(min1)
        for num in nums:
            max2 = max(max2, num)
            min2 = min(min2, num)
    
        print(max1, max2, min1, min2)
        return (max1*max2) - (min1*min2)