class Solution:
    def check(self, nums: List[int]) -> bool:
        #act as if array wraps around, traverse from min element until you get back to min
        #Time -- iterate through array twice -- O(n)
        #Space -- no new arr O(1)
        min_i=-1
        min_num= min(nums)
        for i, num in enumerate(nums):
            if num == min_num:
                min_i=i
                break
        prev=-1
        i= min_i+1
        n= len(nums)
        curr= nums[i%n]
        while (i+1)%n != min_i:
            if nums[(i+1)%n]<nums[i%n]:
                return False
            i+=1

        return True