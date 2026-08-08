class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum, currSum = 0, 0
        lastNum = 0
        for num in nums:
            if lastNum >= num:
                currSum = 0
            
            currSum += num
            maxSum = max(currSum, maxSum)
            lastNum = num
        return maxSum

            