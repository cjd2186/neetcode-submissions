#Algo
'''
two pointers, one for each part of pair
First pointer and second pointer must be equal
If equal, mark negative second part of pair from array (prevents left pointer from double counting)
If not equal, advance right pointer until equal or end of array
'''
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == nums[right] and nums[left] > 0:
                nums[right]*=-1
                left +=1
                right = left+1
            elif nums[left] < 0:
                left +=1
                right +=1
            else:
                right +=1
        #half of the array should be negative if theyre all paired up
        n = len(nums)/2
        negatives = 0
        for num in nums:
            if num < 0:
                negatives+=1
        if negatives == n:
            return True
        else:
            return False
