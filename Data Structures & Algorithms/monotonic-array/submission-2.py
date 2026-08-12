class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #first decide is mono inc or dec
        #check condition is held throughout rest of the array
        # time O(n) go through nums once
        #space O(1) no new arr
        condition = 0
        prev = nums[0]
        n = len(nums)
        for i in range (1,n):
            curr= nums[i]
            if not condition:
                if prev < curr:
                    condition = 1
                if prev > curr:
                    condition = -1
            if condition==1:
                if prev > curr:
                    return False
            if condition==-1:
                if prev < curr:
                    return False
            prev=curr
        return True
                