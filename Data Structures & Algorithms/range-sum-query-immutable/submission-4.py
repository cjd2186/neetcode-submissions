#prefix sum solution
# new array stores the sum of elements to its left

#access each element in the prefix from left to right range in O(1) time and add them to total
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right+1):
            total += self.nums[i]
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)