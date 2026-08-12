#Algo
'''
bit mask to store count of number --> cant because num can be outside of range(n)
#Time: O(nlogn) --> iterate through array once
#Memory: O(1) --> just checking if count is even
'''
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        numCount= 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                numCount +=1
            else:
                if numCount%2 == 1:
                    return False
                numCount = 1
                prev = nums[i]
        return True