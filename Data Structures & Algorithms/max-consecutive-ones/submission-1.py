#Time: 0(n)
#Space: 0(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        curr1 = 0
        for num in nums:
            if num == 1:
                curr1 +=1
            else:
                curr1 = 0
            max1=max(curr1,max1)
        return max1