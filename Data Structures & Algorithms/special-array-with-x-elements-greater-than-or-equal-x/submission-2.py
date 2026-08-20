#Algo
#brute force, go check from 1 to max(nums)
#sort list
#going from 1 to max_num, check is len(nums[num>X:]) == X

#sort nlogn
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        x = -1
        n = max(nums)
        for i in range(1, n+1):
            x = i
            for j, num in enumerate(nums):
                if num >= x:
                    if len(nums) - j == x:
                        return x
                    else:
                        break

        return -1