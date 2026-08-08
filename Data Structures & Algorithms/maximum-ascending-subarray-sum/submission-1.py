
#Algo
#go through nums
# lastNum is greater/equal to current num --> reset currSum to 0
# keep track of maxSum

#Time | Space
# O(n) | O(1)
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum, lastNum, currSum = 0, 0, 0
        for num in nums:
            if lastNum >= num:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)
            lastNum = num
        return maxSum

            