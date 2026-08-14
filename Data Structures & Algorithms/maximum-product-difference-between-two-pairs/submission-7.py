#want to find 2 max ints and 2 min ints --> 4 passes
#Time: O(n) -- pass 4 times
#Space: O(1)
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = -1
        max2 = -1
        min1 = 100001
        min2 = 100002

        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
    
        return (max1*max2) - (min1*min2)